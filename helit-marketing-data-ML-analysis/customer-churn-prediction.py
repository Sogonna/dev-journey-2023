# customer-churn-prediction.py
# Late 2023 - First Machine Learning Project: Churn Prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('customer-data.csv')

X = df[['recency', 'frequency', 'monetary', 'total_orders', 'avg_order_value']]
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Churn Prediction Model Performance:")
print("Accuracy:", round(accuracy_score(y_test, pred), 3))
print("\nClassification Report:\n", classification_report(y_test, pred))

# Feature Importance
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop Important Features:")
print(importances)