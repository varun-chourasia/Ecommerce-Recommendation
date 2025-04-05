import sqlite3
import pandas as pd

# Database file
DB_FILE = "ecommerce_recommendations.db"

# Load CSV files
customer_data = pd.read_csv("data\customer_data_collection.csv")
product_data = pd.read_csv("data\product_recommendation_data.csv")

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    Customer_ID TEXT PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Gender TEXT,
    Location TEXT,
    Browsing_History TEXT,
    Purchase_History TEXT
)
""")

# Create Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    Product_ID TEXT PRIMARY KEY,
    Name TEXT,
    Category TEXT,
    Price REAL,
    Description TEXT,
    Popularity_Score REAL
)
""")

# Create Recommendations Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS recommendations (
    Customer_ID TEXT,
    Recommended_Product_ID TEXT,
    Score REAL,
    FOREIGN KEY(Customer_ID) REFERENCES customers(Customer_ID),
    FOREIGN KEY(Recommended_Product_ID) REFERENCES products(Product_ID)
)
""")

# Insert Data into Customers Table
customer_data.to_sql("customers", conn, if_exists="replace", index=False)

# Insert Data into Products Table
product_data.to_sql("products", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("✅ SQLite Database Setup Completed!")
