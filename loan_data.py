import pandas as pd
import numpy as np


np.random.seed(42)

data = {
    "Gender": np.random.randint(0,2,100),
    "Married": np.random.randint(0,2,100),
    "Education": np.random.randint(0,2,100),
    "Income": np.random.randint(0,2,100),
    "LoanAmount": np.random.randint(0,2,100)
}

df = pd.DataFrame(data)


# Sample rule approval

df["Loan_Status"] = ((df["Income"] > 4000) & (df["LoanAmount"] < 250)).astype(int)

df.to_csv("loan_data.csv", index=False)

print("Dataset Created Successfully!")