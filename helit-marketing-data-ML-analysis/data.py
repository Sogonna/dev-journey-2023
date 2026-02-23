import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)


# ۱. Customer Data 2023 (پیشرفته)
n_customers = 2500
customers = pd.DataFrame({
    'customer_id': range(10001, 10001 + n_customers),
    'first_purchase_date': pd.to_datetime(np.random.choice(pd.date_range('2022-01-01', '2023-06-01'), n_customers)),
})

customers['last_purchase_date'] = customers['first_purchase_date'] + pd.to_timedelta(
    np.random.randint(30, 650, n_customers), unit='d'
)
customers['last_purchase_date'] = customers['last_purchase_date'].clip(upper=pd.to_datetime('2023-12-31'))

customers['total_orders'] = np.random.randint(3, 28, n_customers)
customers['total_spent'] = np.random.uniform(1200000, 52000000, n_customers).round(0)
customers['avg_order_value'] = (customers['total_spent'] / customers['total_orders']).round(0)

snapshot = datetime(2024, 1, 1)
customers['recency'] = (snapshot - customers['last_purchase_date']).dt.days
customers['frequency'] = customers['total_orders']
customers['monetary'] = customers['total_spent']
customers['churn'] = (customers['recency'] > 110).astype(int)   # label برای Churn

customers.to_csv('customer-data.csv', index=False, encoding='utf-8-sig')

# ۲. Sales Transactions 2023
n_sales = 8500
sales = pd.DataFrame({
    'date': pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2023-12-31'), n_sales)),
    'customer_id': np.random.choice(customers['customer_id'], n_sales),
    'product_name': np.random.choice(['Oversize Hoodie', 'Slim Jeans', 'Summer Dress', 'Leather Jacket', 
                                      'Basic T-Shirt', 'Cargo Pants', 'Knit Scarf', 'Denim Jacket'], n_sales),
    'quantity': np.random.randint(1, 6, n_sales),
    'unit_price': np.random.uniform(450000, 3200000, n_sales).round(0)
})
sales['total_revenue'] = sales['quantity'] * sales['unit_price']
sales.to_csv('sales-transactions.csv', index=False, encoding='utf-8-sig')

# ۳. Product Reviews 2023 (با متن فارسی واقعی)
n_reviews = 1200
review_texts = [
    "کیفیت پارچه عالی بود، دقیقاً مثل عکس بود", "اندازه‌اش خیلی کوچیک بود، ناراضی‌ام",
    "رنگش فوق‌العاده قشنگه، بعد شستشو هم نرنگ شد", "خیلی راحت و خوشگل، برای هر موقعیتی مناسبه",
    "دوختش ضعیف بود، بعد دو بار پوشیدن باز شد", "ارزش خرید بالایی داشت، پیشنهاد می‌کنم",
    "گرون بود ولی کیفیتش حرف نداشت", "عالی بود، همه ازم پرسیدن از کجا خریدم",
    "برای زمستون خیلی نازکه", "خیلی خوشگل بود ولی سایزبندی‌اش بد بود"
]

reviews = pd.DataFrame({
    'review_id': range(60001, 60001 + n_reviews),
    'product_name': np.random.choice(['Oversize Hoodie Black', 'Slim Jeans Blue', 'Summer Cotton Dress', 
                                      'Leather Jacket Brown', 'Basic White T-Shirt'], n_reviews),
    'rating': np.random.randint(1, 6, n_reviews),
    'date': pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2023-12-20'), n_reviews)),
    'review_text': np.random.choice(review_texts, n_reviews)
})

reviews.to_csv('product-reviews.csv', index=False, encoding='utf-8-sig')
