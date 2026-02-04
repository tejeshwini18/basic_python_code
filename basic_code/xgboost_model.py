

import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd


# Read in the dataset
#Target : is_canceled: Binary variable indicating whether a booking was canceled
bookings = pd.read_csv('https://raw.githubusercontent.com/datacamp/Machine-Learning-With-XGboost-live-training/master/data/hotel_bookings_clean.csv')

# List out our columns
bookings.info()

# Prepare features and target
y = bookings['is_canceled']
X = bookings.drop('is_canceled', axis=1)

# Encode categorical columns and handle missing values
X = pd.get_dummies(X, drop_first=True)
X = X.fillna(0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build XGBoost model
model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42, n_estimators=100)
model.fit(X_train, y_train)

# Predict and evaluate the model
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))