import pandas as pd

def calculate_roas(tracking_df, payouts_df):

    # Merge payouts into tracking based on influencer_id
    merged = tracking_df.merge(
        payouts_df[['influencer_id', 'total_payout']], 
        on='influencer_id', 
        how='left'
    )

    # Calculate ROAS
    merged['ROAS'] = merged['revenue'] / merged['total_payout']

    # Return a useful subset
    roas_df = merged[['influencer_id', 'campaign', 'total_payout', 'ROAS']]
    return roas_df
    
def top_influencers_by_revenue(tracking_df):
    return tracking_df.groupby('influencer_id')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)    
    
def poor_performers(roas_df, baseline=1.0):
    return roas_df[roas_df['ROAS'] < baseline]
    
def incremental_roas(tracking_df):
    # Dummy baseline revenue
    baseline = 500  
    tracking_df['incremental_ROAS'] = (tracking_df['revenue'] - baseline) / tracking_df['orders'].replace(0, 1)
    return tracking_df[['influencer_id', 'campaign', 'incremental_ROAS']]
    
