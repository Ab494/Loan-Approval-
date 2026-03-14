# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib


# Load sample csv dataset 

data = pd.read_csv("loan_data.csv") # Columns: Gender, Married, Education, Income, Loan_amount and Loan_status

# Encode categorial Columns
le = LabelEncoder()

for col in ['Gender', 'Married', 'Education']:
    data[col] = le.fit_transform(data[col])


# Features and target

X = data[['Gender', 'Married', 'Education', 'Income', 'LoanAmount']]
y = data['Loan_Status'] # 1 = Approved, 0 = Rejected

# Train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train model

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Save the trained model
joblib.dump(model, "app/model.pkl")
print("Model trained and saved Successfully!")