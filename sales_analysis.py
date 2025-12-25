import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/sales_data.csv")

# Convert date column
df["order_date"] = pd.to_datetime(df["order_date"])

# Create total amount
df["total_amount"] = df["quantity"] * df["price"]

# Clean data
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Monthly sales
df["month"] = df["order_date"].dt.to_period("M")
monthly_sales = df.groupby("month")["total_amount"].sum()

# Category sales
category_sales = df.groupby("category")["total_amount"].sum()

# Create output folder
os.makedirs("output", exist_ok=True)

# Plot monthly sales
monthly_sales.plot(kind="line", title="Monthly Sales Trend")
plt.savefig("output/monthly_sales.png")
plt.clf()

# Plot category sales
category_sales.plot(kind="bar", title="Sales by Category")
plt.savefig("output/category_sales.png")
plt.clf()

# Save summary
summary = pd.DataFrame({
    "Total Sales": [df["total_amount"].sum()],
    "Average Sale": [df["total_amount"].mean()]
})
summary.to_csv("output/summary.csv", index=False)

print("Sales analysis completed successfully!")
