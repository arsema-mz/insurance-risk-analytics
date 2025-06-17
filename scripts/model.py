import pandas as pd
from sklearn.model_selection import train_test_split


file_path = 'data/MachineLearningRating_v3.txt'  
data = pd.read_csv(file_path, delimiter='|')  

# Step 1: Filter policies with claims > 0
severity_data = data[data['TotalClaims'] > 0].copy()

# Step 2: Handle missing values - example: drop rows with missing target
severity_data.dropna(subset=['TotalClaims'], inplace=True)

# Step 3: Feature engineering - example: extract year/month from TransactionMonth
severity_data['TransactionMonth'] = pd.to_datetime(severity_data['TransactionMonth'])
severity_data['TransactionYear'] = severity_data['TransactionMonth'].dt.year
severity_data['TransactionMonthNum'] = severity_data['TransactionMonth'].dt.month

# Step 4: Encode categorical features - example: one-hot encoding for Province
severity_data = pd.get_dummies(severity_data, columns=['Province', 'Gender', 'VehicleType'], drop_first=True)

# Step 5: Define features and target
features = severity_data.drop(columns=['TotalClaims', 'PolicyID', 'TransactionMonth'])  # drop unneeded columns
target = severity_data['TotalClaims']

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Train Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict
y_pred = lr.predict(X_test)

# Evaluate
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Linear Regression RMSE: {rmse:.2f}")
print(f"Linear Regression R2: {r2:.2f}")
