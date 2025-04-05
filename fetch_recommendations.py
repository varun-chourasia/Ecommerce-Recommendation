import sqlite3
import json

# Database file
db_file = "ecommerce_recommendations.db"

def fetch_recommendations(customer_id):
    """Fetch recommendations for a given customer."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Recommended_Product_ID, Score FROM recommendations
    WHERE Customer_ID = ?
    ORDER BY Score DESC
    """, (customer_id,))
    
    recommendations = cursor.fetchall()
    conn.close()
    
    if not recommendations:
        return json.dumps({"message": "No recommendations available for this customer."}, indent=4)
    
    # Format results
    results = [{"product_id": rec[0], "score": rec[1]} for rec in recommendations]
    
    return json.dumps(results, indent=4)

# Example usage
if __name__ == "__main__":
    customer_id = input("Enter Customer ID: ")  # Take input from user
    print(fetch_recommendations(customer_id))
