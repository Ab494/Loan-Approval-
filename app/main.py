from fastapi import FastAPI # Created a web API
from pydantic import BaseModel # validate user input
import joblib # Load the trained model 
import numpy as np 

# LOad the saved model

model = joblib.load("app/model.pkl")

# Creating the API application
app  = FastAPI(title = "Loan Approval Prediction API")

class LoanApplication(BaseModel):
    Gender: int
    Married: int
    Education: int
    Income: int
    LoanAmount: int

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Loan Approval API, its Running"}

# Prediction endpoint
@app.post("/predict")
def predict_loan(application: LoanApplication):
    data = np.array([[application.Gender, 
                      application.Married, 
                      application.Education, 
                      application.Income,
                      application.LoanAmount]])

# making prediction
    prediction = model.predict(data)

# converting prediction to human language
    status = "Approved" if prediction[0]==1 else "Rejected"
    return {"status": status}



