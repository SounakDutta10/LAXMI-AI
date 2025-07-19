import streamlit as st
import requests
import matplotlib.pyplot as plt
import yfinance as yf

# Set page config
st.set_page_config(page_title="LakshmiAI", page_icon="💰")

# Title
st.title("💰 LakshmiAI - Your Personal Investment Advisor")
st.markdown("Get personalized investment advice based on your age, income, and goals — powered by AI, ML & LLM.")

# Input Fields
age = st.slider("👤 Your Age", min_value=18, max_value=65, value=25)
income = st.number_input("💵 Monthly Income (₹)", min_value=5000, max_value=200000, value=30000, step=1000)
goal = st.text_input("🎯 Investment Goal (e.g., Retirement, Travel, House)")

# Button to Get Advice
if st.button("Get My Investment Plan"):
    try:
        # Send request to backend
        response = requests.post("http://localhost:8000/predict", json={
            "age": age,
            "income": income,
            "goal": goal
        })

        if response.status_code == 200:
            data = response.json()

            # ✅ Display Risk Profile
            st.subheader("📊 Your Risk Profile")
            st.success(f"**{data['risk_profile']}**")

            # ✅ Display Recommendations
            st.subheader("📈 Recommended Investments")
            for category, items in data["recommendation"].items():
                st.markdown(f"**{category}**:")
                for item in items:
                    st.markdown(f"- {item}")

            # ✅ Display Explanation
            st.subheader("🧠 AI Explanation")
            st.info(data["explanation"])

            # ✅ NAV/Stock Price Chart
            st.subheader("📉 Price Trend of Example Investment (TCS)")

            # You can replace 'TCS.NS' with any other stock/mutual fund ticker like 'INF846K01IE2.BO' for Axis Bluechip
            ticker = yf.Ticker("TCS.NS")
            hist = ticker.history(period="6mo")

            fig, ax = plt.subplots()
            ax.plot(hist.index, hist["Close"], color='green')
            ax.set_title("TCS - 6 Month Price History")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price (₹)")
            ax.grid(True)
            st.pyplot(fig)

            # ✅ Show Latest Price
            latest_price = hist["Close"].iloc[-1]
            st.success(f"🟢 Latest Price (as of {hist.index[-1].date()}): ₹{latest_price:.2f}")

        else:
            st.error("❌ Failed to get response from the backend.")

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to backend. Please make sure FastAPI is running on http://localhost:8000")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
