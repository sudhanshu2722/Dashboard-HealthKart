import pandas as pd

def df_influencers():
    df_influencers = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\influencers.csv")
    return df_influencers

def df_payouts():
    df_payouts = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\payouts.csv")
    return df_payouts

def df_posts():
    df_posts = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\posts.csv")
    return df_posts

def df_tracking():
    df_tracking = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\tracking_data.csv")
    return df_tracking