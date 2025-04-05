import pandas as pd

# Load datasets
customer_df = pd.read_csv("data\customer_data_collection.csv")
product_df = pd.read_csv("data\product_recommendation_data.csv")

# Remove unnecessary columns
customer_df = customer_df.drop(columns=["Unnamed: 10"], errors="ignore")
product_df = product_df.drop(columns=["Unnamed: 13", "Unnamed: 14"], errors="ignore")

# Convert Browsing & Purchase History to list format
customer_df["Browsing_History"] = customer_df["Browsing_History"].apply(lambda x: eval(x) if isinstance(x, str) else [])
customer_df["Purchase_History"] = customer_df["Purchase_History"].apply(lambda x: eval(x) if isinstance(x, str) else [])

# Extract relevant product categories
category_mapping = product_df.set_index("Product_ID")["Category"].to_dict()

# Save cleaned data
customer_df.to_csv("cleaned_customer_data.csv", index=False)
product_df.to_csv("cleaned_product_data.csv", index=False)

print("✅ Data Cleaning & Feature Extraction Completed!")
