import pandas as pd

# Creating a new dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rajesh", "Meena", "Suresh", "Anita", "Vijay", "Neeta"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Age": [29, 35, 45, 32, 50, 28],
    "Salary": [70000, 85000, 95000, 64000, 120000, 72000],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Exercise 1: Rename Columns
df.rename(columns={"Salary": "Annual Salary", "City": "Location"}, inplace=True)
print("\nDataFrame after renaming columns:\n", df)

# Exercise 2: Drop Columns
df.drop(columns=["Location"])
print("\nDataFrame after dropping 'Location' column:\n", df)

# Exercise 3: Drop Rows
df.drop(index=2)
print("\nDataFrame after dropping the row where Name is 'Suresh':\n", df)

# Exercise 4: Handle Missing Data
df.loc[df["Name"] == "Meena", "Annual Salary"] = None  # Assign None to Meena's salary
mean_salary = df["Annual Salary"].mean()  # Calculate the mean salary
df["Annual Salary"].fillna(mean_salary, inplace=True)  # Fill the missing value with the mean salary
print("\nDataFrame after handling missing data:\n", df)

# Exercise 5: Create Conditional Columns
df["Seniority"] = df["Age"].apply(lambda x: "Senior" if x >= 40 else "Junior")
print("\nDataFrame after adding 'Seniority' column:\n", df)

# Exercise 6: Grouping and Aggregation
grouped_df = df.groupby("Department")["Annual Salary"].mean().reset_index()
print("\nAverage salary by department:\n", grouped_df)
