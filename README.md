# healthkart-dashboard
Influencer campaign ROI and ROAS tracking dashboard using Streamlit


# HealthKart Influencer Campaign Dashboard 📊

A Streamlit-powered interactive dashboard to analyze and visualize influencer marketing campaign performance for HealthKart.

**Live Demo**: 👉 [sudhanshu2722-dashboard-healthkart.streamlit.app](https://sudhanshu2722-dashboard-healthkart.streamlit.app)

---

## 📌 Overview

This project provides marketing stakeholders with a centralized platform to:
- Monitor **Return on Ad Spend (ROAS)** and **Incremental ROAS**
- Identify **top-performing** and **underperforming** influencers
- Drill down by **brand**, **product**, and **influencer type**
- Visualize **revenue trends**, platform impact, and ROI metrics

The dashboard is modular, production-ready, and deployed on **Streamlit Cloud**.

---

## 🧱 Project Structure

```bash
.
├── healthkart/                     # Virtual environment
├── input_data/                    # Data generation module
│   └── dataset_creation.py
├── src/                           # Core logic
│   ├── analytics.py               # Metric calculations
│   ├── data_loader.py             # Dataset loading functions
│   ├── utils.py                   # Helper functions
│   └── visualization.py           # Streamlit visual elements
├── app.py                         # Main Streamlit app
├── requirements.txt               # Dependencies
├── .gitignore
├── README.md                      # This file
├── Influencers.csv
├── Posts.csv
├── Payouts.csv
└── Tracking_data.csv


⚙️ FEATURES

📈 ROAS & Incremental ROAS: Analyze efficiency of spend
🧍 Influencer Segmentation: Filter by type, persona, and platform
🥇 Top/Bottom Performer Cards: Instant insights on campaign ROI
📊 Visualizations: Revenue charts, metric comparison, platform insights
🧾 CSV Download and (optional) PDF export for reports
📁 Modular Architecture: Clean separation of logic (loading, processing, UI)


HOW TO CLONE REPOSITORY?
git clone https://github.com/sudhanshu2722/Dashboard-HealthKart.git
cd Dashboard-HealthKart


VIRTUAL ENVIRONMENT
python -m venv healthkart
healthkart\Scripts\activate


HOW TO INSTALL DEPENDENCIES?
pip install -r requirements.txt


HOW TO RUN APP?
streamlit run app.py

🚀 Deployment
This project is deployed on Streamlit Cloud at:

🌐 https://sudhanshu2722-dashboard-healthkart.streamlit.app

Deployment Steps:
1) Push your final changes to the main branch of your GitHub repo
2) Connect the repo to Streamlit Cloud
3) Set app.py as the entry point and deploy!

🧠 Insights & Learnings
1) Learned how to structure and modularize a real-world dashboard project
2) Implemented marketing-specific KPIs like ROAS and platform ROI
3) Gained experience with Streamlit deployment and environment setup
4) Addressed common issues like path dependency for cloud deployment

📧 Contact
Sudhanshu Upadhyay
mail address : bhanuupadhyay302448@gmail.com
🧑‍💻 GitHub: sudhanshu2722