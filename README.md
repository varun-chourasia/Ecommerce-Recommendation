# **AI-Powered E-Commerce Product Recommendation System** 🚀  

This project is a **multi-agent AI system** that provides personalized **e-commerce product recommendations** using **machine learning models and AI agents**.  

## **🔹 Features**  
✅ Personalized product recommendations based on customer behavior  
✅ Hybrid recommendation engine (collaborative + content-based filtering)  
✅ AI-powered analysis of customer data and product similarities  
✅ Intuitive UI built with **Streamlit**  

## **📂 Project Structure**  
```
HACKATHON_PROJECT/
│── data/                       # Dataset folder
│   ├── customer_data_collection.csv
│   ├── product_recommendation_data.csv
│── data_preprocessing.py        # Preprocessing script
│── ecommerce_recommendations.db  # SQLite database
│── fetch_recommendations.py     # Fetch recommendations from DB
│── generate_recommendation.py   # Generate recommendations
│── setup_db.py                  # Database setup script
│── ui.py                        # Streamlit UI app
│── verify_db.py                 # DB verification script
│── README.md                    # Project documentation
```

## **💻 Installation**  
### **1️⃣ Clone the repository**  
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### **2️⃣ Create a virtual environment & install dependencies**  
```bash
python -m venv venv  
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit app**  
```bash
streamlit run ui.py
```

## **🚀 Deployment**  
1️⃣ Push the code to **GitHub**  
2️⃣ Deploy on **Streamlit Community Cloud**  
3️⃣ Set `ui.py` as the main entry point  

---

## **👨‍💻 Technologies Used**  
🔹 **Python**  
🔹 **Streamlit** (UI)  
🔹 **SQLite** (Database)  
🔹 **Machine Learning Models**  
🔹 **LangChain / CrewAI** (Agent-based coordination)  

---

## **📝 License**  
This project is **open-source** and can be modified as per requirements.  

🔗 **Live Demo:** [Deployed App Link](https://your-streamlit-app-url)  

