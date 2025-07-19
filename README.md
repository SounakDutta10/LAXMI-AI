# 💰 LakshmiAI — Your Personal AI Financial Advisor 🇮🇳

**LakshmiAI** is a personalized financial advisory tool designed for Indian retail investors. It uses **Machine Learning**, **NLP**, and **LLM-style explanations** to offer tailored investment advice based on your age, income, and goals.

Built with:
- 🧠 FastAPI (Backend)
- 🎨 Streamlit (Frontend)
- 📊 yFinance & Matplotlib (Live price trends)
- 💬 AI-generated recommendations and explanations (LLM-style)

---

## 🚀 Features

✅ Predicts user **risk profile** (Conservative / Balanced / Aggressive)  
✅ Provides **SIP, Debt, Stock, and Crypto** investment recommendations  
✅ Includes **AI-generated, human-like financial explanations**  
✅ Fetches and visualizes **real NAV/stock price trends** via yFinance  
✅ Interactive UI using Streamlit  
✅ Modular backend using FastAPI (easy to upgrade to real ML/LLMs)

---




## 🏗️ Project Structure

```
lakshmiai/
├── backend/
│   ├── app.py               # FastAPI server
│   ├── recommender.py       # Risk profiling + recommendations
│   ├── gpt_advisor.py       # LLM-style AI explanation generator
│   └── models/              # Placeholder for ML models (optional)
├── frontend/
│   └── app.py               # Streamlit frontend app
├── requirements.txt         # All Python dependencies
└── README.md                # This file
```

---

## 🧠 How It Works

1. **User Input**: Age, Monthly Income, and Investment Goal  
2. **Risk Profiling**:
   - Based on rule-based logic (can be replaced with ML model)
   - Categories: Conservative, Balanced, Aggressive  
3. **Recommendations**:
   - Mutual funds, debt funds, stocks, crypto (mock data or can be linked to APIs)  
4. **AI Explanation**:
   - Human-like investment logic generated in `gpt_advisor.py`  
5. **NAV Trend Graph**:
   - yFinance is used to show 6-month price trend of key recommendations  

---

## 💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/lakshmiai.git
cd lakshmiai
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Start the Backend (FastAPI)

```bash
cd backend
uvicorn app:app --reload
```

Confirm it's working:  
👉 http://localhost:8000/docs

### 4. Start the Frontend (Streamlit)

Open a **new terminal**:

```bash
cd frontend
streamlit run app.py
```

---

## 📊 Sample Output

- **Risk Profile**: Conservative  
- **Recommendations**:
  - SIP: Axis Bluechip Fund
  - Debt: HDFC Corporate Bond Fund  
- **AI Explanation**:
  > "Based on your age, income, and investment goal, we’ve categorized you as a **Conservative Investor**. This means your priority is capital protection with steady, low-risk growth..."

---

## 📦 Dependencies

- `fastapi`
- `uvicorn`
- `streamlit`
- `yfinance`
- `matplotlib`
- `scikit-learn`
- `requests`
- `pandas`

Install all using:
```bash
pip install -r requirements.txt
```

---

## ✨ Future Enhancements

- 🔁 Plug in GPT-4 or OpenAI API for real-time explanation  
- 📊 Portfolio simulation with expected return/CAGR  
- 🔍 Goal-based investment planning (e.g., retirement, child’s education)  
- ☁️ Deploy on Streamlit Cloud / Render / Hugging Face Spaces  

---

## 📜 License

MIT License © 2025 — [Your Name](https://github.com/SounakDutta10)

---

## 🙏 Acknowledgments

- AMFI, NSE, and SEBI for regulatory insights  
- yFinance for live financial data  
- OpenAI and Streamlit for the foundation tech stack  
- Built with ❤️ in India
