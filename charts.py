import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------------
# Monthly Sales (Line Chart)
# -----------------------------------

monthly = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(8,5))
plt.plot(monthly.index.astype(str), monthly.values, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

# -----------------------------------
# Quarterly Sales (Line Chart)
# -----------------------------------

quarterly = df.groupby(df["Date"].dt.to_period("Q"))["Sales"].sum()

plt.figure(figsize=(8,5))
plt.plot(quarterly.index.astype(str), quarterly.values, marker="o")
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("quarterly_sales.png")
plt.close()

# -----------------------------------
# Category Sales (Bar Chart)
# -----------------------------------

category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,5))
plt.bar(category.index, category.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

# -----------------------------------
# Category Share (Pie Chart)
# -----------------------------------

plt.figure(figsize=(6,6))
plt.pie(
    category.values,
    labels=category.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Category Share")
plt.tight_layout()
plt.savefig("category_share.png")
plt.close()

# -----------------------------------
# Export Summary
# -----------------------------------

summary = f"""
SALES SUMMARY

Total Sales : {df['Sales'].sum()}

Average Sales : {df['Sales'].mean():.2f}

Highest Sale : {df['Sales'].max()}

Lowest Sale : {df['Sales'].min()}

Best Category : {category.idxmax()}

Best Month : {monthly.idxmax()}
"""

with open("summary.txt", "w") as file:
    file.write(summary)

print("Project Completed Successfully!")