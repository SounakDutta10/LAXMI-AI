import pandas as pd
from sklearn.cluster import KMeans

def predict_risk(age, income, goal):
    data = pd.DataFrame([[age, income]], columns=["age", "income"])
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit([[20, 20000], [30, 40000], [40, 70000]])
    cluster = kmeans.predict(data)[0]
    return ["Conservative", "Balanced", "Aggressive"][cluster]

def get_recommendation(risk_type):
    if risk_type == "Conservative":
        return {"SIP": ["Axis Bluechip Fund"], "Debt": ["HDFC Corporate Bond Fund"]}
    elif risk_type == "Balanced":
        return {"MF": ["ICICI Balanced Advantage Fund"], "Stocks": ["TCS", "HUL"]}
    else:
        return {"Stocks": ["Tata Motors", "Zomato"], "Crypto": ["BTC (5% max)"]}