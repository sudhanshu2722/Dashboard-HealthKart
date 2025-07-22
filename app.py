import streamlit as st
from src.data_loader import df_influencers, df_payouts, df_posts, df_tracking
from src.analytics import calculate_roas, top_influencers_by_revenue, poor_performers, incremental_roas
from src.visualization import show_bar_chart
from src import data_loader
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="HealthKart Dashboard", layout="wide")

st.title("📊 HealthKart Influencer Campaign Dashboard")

# Load Data
influencers, posts, tracking, payouts = df_influencers(), df_posts(), df_tracking(), df_payouts()

# =========================
# Sidebar Filters
# =========================
st.sidebar.header("🔎 Filter Options")

# ✅ Platform Filter
platform_filter = st.sidebar.selectbox("Platform", options=["All"] + influencers['platform'].dropna().unique().tolist())
if platform_filter != "All":
    influencers = influencers[influencers['platform'] == platform_filter]
    tracking = tracking[tracking['influencer_id'].isin(influencers['id'])]

# ✅ Influencer Type Filter
if 'persona' in influencers.columns:
    type_filter = st.sidebar.multiselect("Influencer Type", options=influencers['persona'].dropna().unique())
    if type_filter:
        influencers = influencers[influencers['persona'].isin(type_filter)]
        tracking = tracking[tracking['influencer_id'].isin(influencers['id'])]

# ✅ Product Filter
product_filter = st.sidebar.multiselect("Product", options=tracking['product'].dropna().unique())
if product_filter:
    tracking = tracking[tracking['product'].isin(product_filter)]


# ✅ Baseline ROAS Input
baseline_roas = st.sidebar.number_input(
    "Set your baseline ROAS", min_value=0.0, max_value=10.0, value=1.0, step=0.1, format="%.2f"
)

# =========================
# ROAS Calculation
# =========================
if tracking.empty or payouts.empty:
    st.error("⚠️ No data available for selected filters.")
    st.stop()

roas_df = calculate_roas(tracking, payouts)
incr_roas_df = incremental_roas(tracking)
combined_roas_df = roas_df.merge(incr_roas_df, on=["influencer_id", "campaign"])

# =========================
# Metrics Summary
# =========================
st.markdown("## 📌 Campaign Performance Summary")
total_revenue = tracking['revenue'].sum()
total_payout = payouts['total_payout'].sum()
avg_roas = combined_roas_df['ROAS'].mean()
avg_incr_roas = combined_roas_df['incremental_ROAS'].mean()
num_influencers = combined_roas_df['influencer_id'].nunique()
num_campaigns = combined_roas_df['campaign'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("🏦 Total Payout", f"₹{total_payout:,.0f}")
col3.metric("📊 Avg. ROAS", f"{avg_roas:.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("🚀 Avg. Incremental ROAS", f"{avg_incr_roas:.2f}")
col5.metric("👥 Unique Influencers", num_influencers)
col6.metric("📢 Total Campaigns", num_campaigns)

st.markdown("---")

# =========================
# ROAS Dataframe Display
# =========================
st.header("📈 ROAS & Incremental ROAS")
# Sort ROAS in descending order
combined_roas_df = combined_roas_df.sort_values(by="ROAS", ascending=False).reset_index(drop=True)

# Style ROAS values with background color
def style_roas(val):
    if pd.isna(val):
        return ''
    elif val >= baseline_roas:
        return 'background-color: #d1e7dd; color: black;'  # light green
    else:
        return 'background-color: #f8d7da; color: black;'  # light red

# Apply styling
styled_df = combined_roas_df.style.applymap(style_roas, subset=['ROAS'])

# Show DataFrame
st.dataframe(styled_df, use_container_width=True)


# =========================
# Visual Comparison: ROAS vs Incremental ROAS
# =========================
#st.markdown("### 📉 ROAS vs Incremental ROAS Chart")
import matplotlib.pyplot as plt
import numpy as np

# Get top 15 influencers by ROAS (handle missing/null)
top_influencers = combined_roas_df.dropna(subset=["ROAS"]).nlargest(15, "ROAS")

# Convert influencer IDs to string for x-axis labels
influencers = top_influencers["influencer_id"].astype(str)
roas_values = top_influencers["ROAS"]
inc_roas_values = top_influencers["incremental_ROAS"]

# Set bar width and positions
x = np.arange(len(influencers))
width = 0.35

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, roas_values, width, label='ROAS', color='#007bff')  # Blue
bars2 = ax.bar(x + width/2, inc_roas_values, width, label='Incremental ROAS', color='#ff9800')  # Orange

# Add labels and formatting
ax.set_xlabel("Influencer ID")
ax.set_ylabel("Value")
ax.set_title("Top 15 Influencers: ROAS vs Incremental ROAS")
ax.set_xticks(x)
ax.set_xticklabels(influencers, rotation=45)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Display chart in Streamlit
st.markdown("### 📊 ROAS vs Incremental ROAS Chart")
st.pyplot(fig)


st.markdown("---")

# =========================
# Top Influencers by Revenue
# =========================
st.header("🏆 Top Influencers by Revenue")
top_rev = top_influencers_by_revenue(tracking)
st.dataframe(top_rev)

# =========================
# Poor Performers
# =========================
st.header(f"⚠️ Poor Performing Influencers (ROAS < {baseline_roas})")
poor_df = poor_performers(roas_df, baseline=baseline_roas)
st.dataframe(poor_df)

# =========================
# Bar Chart
# =========================
st.header("📊 Revenue by Influencer")
show_bar_chart(top_rev, x="influencer_id", y="revenue", title="Revenue by Influencer")

# =========================
# Downloads
# =========================
st.download_button("📥 Download ROAS Data (CSV)", roas_df.to_csv(index=False), "roas_data.csv", "text/csv")

# Optional PDF (implement if required)
# from fpdf import FPDF or pdfkit usage
# (You can call a function here to export `combined_roas_df` to PDF)

