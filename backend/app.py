from fastapi import FastAPI
from pydantic import BaseModel
from recommender import predict_risk, get_recommendation
from gpt_advisor import explain_plan

app = FastAPI()

class UserInput(BaseModel):
    age: int
    income: int
    goal: str

@app.post("/predict")
def predict(user: UserInput):
    risk = predict_risk(user.age, user.income, user.goal)
    recommendation = get_recommendation(risk)
    explanation = explain_plan(risk, recommendation)
    return {
        "risk_profile": risk,
        "recommendation": recommendation,
        "explanation": explanation
    }