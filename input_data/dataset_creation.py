import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()
random.seed(42)
np.random.seed(42)

num_records = 1000
platforms = ["Instagram", "YouTube", "Twitter", "Facebook"]
categories = ["Fitness", "Nutrition", "Wellness", "Lifestyle"]
genders = ["Male", "Female"]
products = ["Protein", "Multivitamin", "Creatine", "Omega-3", "Collagen", "Fat Burner"]
basis_types = ["post", "order"]

# influencers.csv
influencers = pd.DataFrame({
    "id": range(1, num_records + 1),
    "name": [fake.first_name() for _ in range(num_records)],
    "category": [random.choice(categories) for _ in range(num_records)],
    "gender": [random.choice(genders) for _ in range(num_records)],
    "follower_count": [random.randint(10000, 500000) for _ in range(num_records)],
    "platform": [random.choice(platforms) for _ in range(num_records)],
})
influencers.to_csv(r"C:\Users\USER\Downloads\healthkart assignment input\Influencers.csv", index=False)

# posts.csv
posts = pd.DataFrame({
    "influencer_id": [random.randint(1, num_records) for _ in range(num_records)],
    "platform": [random.choice(platforms) for _ in range(num_records)],
    "date": [fake.date_between(start_date="-6M", end_date="today") for _ in range(num_records)],
    "url": [fake.url() for _ in range(num_records)],
    "caption": [fake.sentence(nb_words=6) for _ in range(num_records)],
    "reach": [random.randint(5000, 300000) for _ in range(num_records)],
    "likes": [random.randint(100, 20000) for _ in range(num_records)],
    "comments": [random.randint(10, 5000) for _ in range(num_records)],
})
posts.to_csv(r"C:\Users\USER\Downloads\healthkart assignment input\Posts.csv", index=False)

# tracking_data.csv
tracking_data = pd.DataFrame({
    "source": [random.choice(platforms) for _ in range(num_records)],
    "campaign": [f"C{random.randint(1, 10)}" for _ in range(num_records)],
    "influencer_id": [random.randint(1, num_records) for _ in range(num_records)],
    "user_id": [random.randint(1000, 9999) for _ in range(num_records)],
    "product": [random.choice(products) for _ in range(num_records)],
    "date": [fake.date_between(start_date="-6M", end_date="today") for _ in range(num_records)],
    "orders": [random.randint(1, 20) for _ in range(num_records)],
    "revenue": [random.randint(500, 10000) for _ in range(num_records)],
})
tracking_data.to_csv(r"C:\Users\USER\Downloads\healthkart assignment input\Tracking_data.csv", index=False)

# payouts.csv
payouts = pd.DataFrame({
    "influencer_id": random.choices(range(1, num_records + 1), k=num_records),
    "basis": [random.choice(basis_types) for _ in range(num_records)],
    "rate": [random.randint(50, 500) for _ in range(num_records)],
    "orders": [random.randint(1, 100) for _ in range(num_records)],
})
payouts["total_payout"] = payouts.apply(
    lambda row: row["rate"] * (row["orders"] if row["basis"] == "order" else 1), axis=1
)
payouts.to_csv(r"C:\Users\USER\Downloads\healthkart assignment input\Payouts.csv", index=False)

print("Dataset creation done!")