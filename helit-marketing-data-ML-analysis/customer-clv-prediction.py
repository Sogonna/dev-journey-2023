# customer-clv-prediction.py
# Mid 2023 - Customer Lifetime Value Estimation

import pandas as pd

customers = pd.read_csv('customer-data.csv')
sales = pd.read_csv('sales-transactions.csv')

# محاسبه CLV واقعی + تخمینی
clv = customers.copy()
clv['lifetime_days'] = (pd.to_datetime(clv['last_purchase_date']) - pd.to_datetime(clv['first_purchase_date'])).dt.days
clv['avg_monthly_spend'] = clv['total_spent'] / (clv['lifetime_days'] / 30 + 1)

# تخمین CLV برای ۱۲ ماه آینده
clv['predicted_clv_12m'] = clv['avg_monthly_spend'] * 12

print("Top 10 Customers by Predicted CLV:")
print(clv[['customer_id', 'total_spent', 'avg_monthly_spend', 'predicted_clv_12m']]
      .sort_values('predicted_clv_12m', ascending=False).head(10).round(0))

clv.to_csv('clv-results.csv', index=False)
