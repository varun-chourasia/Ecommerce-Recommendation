import streamlit as st
import sqlite3

# Function to fetch product recommendations for a customer
def fetch_recommendations(customer_id):
    conn = sqlite3.connect("ecommerce_recommendations.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Recommended_Product_ID, Score 
        FROM recommendations 
        WHERE Customer_ID = ? 
        ORDER BY Score DESC 
        LIMIT 5
    """, (customer_id,))
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations

# Function to fetch product details
def fetch_product_details(product_id):
    conn = sqlite3.connect("ecommerce_recommendations.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Product_ID, Category, Subcategory, Price, Brand, Product_Rating
        FROM products
        WHERE Product_ID = ?
    """, (product_id,))
    product_details = cursor.fetchone()
    conn.close()
    return product_details

# Streamlit UI Configuration
st.set_page_config(page_title="AI-Powered Recommendations", layout="wide")
st.title("🔍 AI-Powered Product Recommendations")

# Initialize session state
if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

# Input field
customer_id = st.text_input("Enter Customer ID (e.g., C1000):", key="customer_input")

# If a new Customer ID is entered, clear old recommendations
if customer_id != st.session_state.get("current_customer", ""):
    st.session_state.recommendations = None

# Get Recommendations Button
if st.button("Get Recommendations", key="get_recs") and customer_id:
    st.session_state.recommendations = fetch_recommendations(customer_id)
    st.session_state.current_customer = customer_id  # Store the current customer ID

# Display recommendations if available
if st.session_state.recommendations:
    st.subheader(f"✅ Recommendations for Customer: {customer_id}")

    for product_id, score in st.session_state.recommendations:
        product = fetch_product_details(product_id)
        if product:
            product_id, category, subcategory, price, brand, rating = product

            # Display product details as a card
            st.markdown(
                f"""
                <div style="border-radius: 10px; background-color: #2E3B4E; padding: 15px; margin-bottom: 10px; color: white;">
                    <h4>🛒 {product_id} - {brand}</h4>
                    <p>📦 Category: {category} ({subcategory})</p>
                    <p>💲 Price: ${price}</p>
                    <p>⭐ Rating: {round(rating, 1)}</p>
                    <p>🔢 Recommendation Score: {round(score, 2)}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.warning("⚠️ Enter a Customer ID and click 'Get Recommendations' to see results.")
