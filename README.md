# dev-journey-2023

**From marketing dashboards to my first real machine learning experiments – 2023**

By 2023 I was still doing remote marketing work for an Iranian online fashion brand, digging into sales numbers every day.  
But I started feeling like basic charts and averages weren’t telling me the full story anymore.  
I wanted to predict what customers might do next, understand what they really thought about the products, and go beyond just “reporting what happened.”

So I started teaching myself more serious stuff — just me, late-night YouTube videos, Kaggle examples, and a lot of trial and error.

This repo is a collection of those early experiments.  
They’re still pretty basic, full of beginner decisions, but I keep them here because that was exactly where everything started to feel real for me.

### What’s inside 

- **customer-clv-prediction.py**  
  My first attempt at guessing how much a customer might be worth in the long run (Customer Lifetime Value).  
  I took past purchases, calculated average order value and frequency, and projected future spend.

- **customer-churn-prediction.py**  
  The very first time I built a proper machine learning model.  
  Tried to predict which customers were about to leave (churn).  
  Started with Random Forest, then simplified it to Logistic Regression because it was easier to understand what was going on.

- **product-review-sentiment.py**  
  My first dive into working with text (NLP).  
  Took customer reviews of clothes and used TextBlob to figure out if they were mostly positive, negative, or neutral.  
  Plotted the results and realized how much hidden feedback is sitting in comments.

  ### Data Note

All datasets here are simulated but realistic recreations based on the actual marketing and sales data I worked with at the brand in 2023.  
Original records contain confidential customer and financial information, so synthetic versions were created to keep the same scale and patterns.

### Tools I used back then

- Python
- pandas & numpy
- matplotlib & seaborn
- scikit-learn
- TextBlob
