import streamlit as st
import sqlite3

# Function to fetch recommendations
def fetch_recommendations():
    customer_id = st.session_state.customer_input  # Get value from input
    if customer_id:
        st.session_state.submitted = True  # Trigger recommendations
        conn = sqlite3.connect("ecommerce_recommendations.db")
        cursor = conn.cursor()

        # Fetch top 6 recommended products for the given customer ID
        query = """
        SELECT Recommended_Product_ID, Score 
        FROM recommendations 
        WHERE Customer_ID = ? 
        ORDER BY Score DESC 
        LIMIT 6
        """
        cursor.execute(query, (customer_id,))
        recommendations = cursor.fetchall()
        conn.close()

        # Store recommendations in session state
        st.session_state.recommendations = recommendations

# Initialize session state variables
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

# Streamlit UI Components
st.markdown('<h1 style="text-align:center;">🔍 AI-Powered Product Recommendations</h1>', unsafe_allow_html=True)
st.subheader("Enter a Customer ID to Get Personalized Suggestions")

# Input Field with 'Enter' key functionality
customer_input = st.text_input("Enter Customer ID (e.g., C1000)", key="customer_input", on_change=fetch_recommendations)

# Button to fetch recommendations manually
if st.button("Get Recommendations"):
    fetch_recommendations()

# Show recommendations when submitted
if st.session_state.submitted and st.session_state.recommendations:
    st.success(f"✅ Top 6 Recommendations for Customer: {customer_input}")

    # Create rows of 3 cards per row
    cols = st.columns(3)  # 3 columns for even distribution

    for index, (product_id, score) in enumerate(st.session_state.recommendations):
        with cols[index % 3]:  # Arrange in 3-column layout
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #2E2E2E, #1C1C1C);
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0px 10px 25px rgba(255, 215, 0, 0.7);
                    text-align: center;
                    width: 100%;
                    max-width: 550px;  /* Increased width */
                    height: 320px;
                    margin-bottom: 70px;">
                    <h3>🛒 {product_id}</h3>
                    <p>Category: Fashion</p>
                    <p>💰 Price: ${round(score * 1000, 2)}</p>
                    <p>⭐ Rating: {round(score * 5 / 2, 1)}</p>
                    <p>🔥 Score: {round(score, 2)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
