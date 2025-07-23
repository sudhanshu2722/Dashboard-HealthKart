# import pandas as pd

# def df_influencers():
#     df_influencers = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\influencers.csv")
#     return df_influencers

# def df_payouts():
#     df_payouts = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\payouts.csv")
#     return df_payouts

# def df_posts():
#     df_posts = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\posts.csv")
#     return df_posts

# def df_tracking():
#     df_tracking = pd.read_csv(r"C:\Users\USER\Downloads\healthkart assignment input\tracking_data.csv")
#     return df_tracking

import os
import pandas as pd

# Get the absolute path to the project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define relative paths to each CSV
def df_influencers():
    path = os.path.join(BASE_DIR, "Influencers.csv")
    return pd.read_csv(path)

def df_posts():
    path = os.path.join(BASE_DIR, "Posts.csv")
    return pd.read_csv(path)

def df_tracking():
    path = os.path.join(BASE_DIR, "Tracking_data.csv")
    return pd.read_csv(path)

def df_payouts():
    path = os.path.join(BASE_DIR, "Payouts.csv")
    return pd.read_csv(path)
