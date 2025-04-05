import pandas as pd
import sqlite3

conn = sqlite3.connect("ecommerce_recommendations.db")
conn.execute("PRAGMA journal_mode=WAL;")  # Enable Write-Ahead Logging
conn.close()

print("✅ Database unlocked!")

# Load cleaned datasets
print("📂 Loading datasets...")
customer_df = pd.read_csv("cleaned_customer_data.csv")
product_df = pd.read_csv("cleaned_product_data.csv")

# Connect to SQLite Database
print("🔗 Connecting to SQLite database...")
conn = sqlite3.connect("ecommerce_recommendations.db")
cursor = conn.cursor()

# Create recommendations table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS recommendations (
        Customer_ID TEXT,
        Recommended_Product_ID TEXT,
        Score REAL
    )
""")
conn.commit()

# Convert product data into a dictionary for quick lookup
print("📊 Processing product data...")
product_info = product_df.set_index("Product_ID").to_dict(orient="index")

print("🚀 Generating recommendations...")
for idx, customer in customer_df.iterrows():
    customer_id = customer["Customer_ID"]
    print(f"🔍 Processing customer: {customer_id} ({idx+1}/{len(customer_df)})")

    try:
        browsing_history = eval(customer["Browsing_History"]) if isinstance(customer["Browsing_History"], str) else []
        purchase_history = eval(customer["Purchase_History"]) if isinstance(customer["Purchase_History"], str) else []
    except Exception as e:
        print(f"❌ Error parsing history for {customer_id}: {e}")
        continue  # Skip this customer if there's an issue

    recommended_products = []

    for product_id, product_data in product_info.items():
        try:
            if product_data["Category"] in browsing_history or product_data["Category"] in purchase_history:
                score = (
                    product_data["Probability_of_Recommendation"] * 0.5 +
                    product_data["Product_Rating"] * 0.3 +
                    product_data["Customer_Review_Sentiment_Score"] * 0.2
                )
                recommended_products.append((product_id, score))
        except Exception as e:
            print(f"⚠️ Error processing product {product_id}: {e}")

    # Sort recommendations by score (highest first)
    recommended_products = sorted(recommended_products, key=lambda x: x[1], reverse=True)[:5]  # Top 5

    # Store recommendations in SQLite
    for product_id, score in recommended_products:
        cursor.execute("INSERT INTO recommendations VALUES (?, ?, ?)", (customer_id, product_id, score))
    
    conn.commit()  # Save after each customer to prevent data loss

print("✅ Recommendations Generated & Stored in SQLite!")
conn.close()
