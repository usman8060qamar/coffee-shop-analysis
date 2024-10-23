import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.express as px

# Step 1: Load Excel File (direct reference to file in the same folder)
df = pd.read_excel('Cleaned_Coffee_Shop_Sales.xlsx')

# Step 2: Calculate Total Sales
df['Total_Sales'] = df['transaction_qty'] * df['unit_price']

# Step 3: Product-wise Sales Comparison
sales_by_product = df.groupby('product_category')['Total_Sales'].sum().reset_index()

# Visualize Product-wise Sales
plt.figure(figsize=(10, 6))
sns.barplot(x='product_category', y='Total_Sales', data=sales_by_product)
plt.xticks(rotation=45)
plt.title('Total Sales by Product Category')
plt.show()

# Step 4: Sales Forecasting (Predict Future Sales)
# Convert date column to datetime and prepare features/target
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['transaction_ordinal'] = df['transaction_date'].apply(lambda x: x.toordinal())  # Convert date to ordinal

X = df[['transaction_ordinal']]  # Features (dates as ordinal numbers)
y = df['Total_Sales']  # Target (Total Sales)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future sales
y_pred = model.predict(X_test)

# Visualize actual vs predicted sales
plt.figure(figsize=(10, 6))
plt.plot(X_test, y_test, label='Actual Sales')
plt.plot(X_test, y_pred, label='Predicted Sales', linestyle='--')
plt.legend()
plt.title('Actual vs Predicted Sales')
plt.show()

# Step 5: Loss Mitigation (Analyzing Low Sales Products)
# Filter products with low sales (if any)
low_sales_products = df[df['Total_Sales'] < 100]  # Assuming low sales are under 100

# Group by product_category to identify low sales patterns
low_sales_by_product = low_sales_products.groupby('product_category')['Total_Sales'].sum().reset_index()

# Print the low sales products and their total sales
print(low_sales_by_product)

# Step 6: Bonus - Interactive Sales Visualization with Plotly
fig = px.bar(sales_by_product, x='product_category', y='Total_Sales', title='Total Sales by Product Category')
fig.show()
