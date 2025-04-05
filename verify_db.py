import sqlite3

DB_FILE = "ecommerce_recommendations.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

customer_id = "C1000"

cursor.execute("SELECT * FROM recommendations WHERE Customer_ID = ?", (customer_id,))
result = cursor.fetchall()

if result:
    print("✅ Customer Found:", result)
else:
    print("❌ Customer Not Found")

conn.close()
