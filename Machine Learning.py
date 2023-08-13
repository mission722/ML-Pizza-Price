import pandas as pd
from sklearn.linear_model import LinearRegression

# Reading Excel File
excel_file_path = 'dataset.xlsx'
data = pd.read_excel(excel_file_path)

# Setting X and Y Values
x = data[['size', 'number of topping']]
y = data['price']

# Fitting the Model
model = LinearRegression()
model.fit(x, y)

# Input data for prediction
print("-" * 65)
size = input(" Enter the size of the pizza \n(options: Small, Medium, Large): ").lower()
print("-" * 65)
Number_of_topping = int(input("Enter how much topping do you need? (e.g., 1, 2, 3, ...): "))
print("-" * 65)

# Converting input to numeric form
if "small" in size:
    order = pd.DataFrame([[0, Number_of_topping]], columns=['size', 'number of topping'])

elif "medium" in size:
    order = pd.DataFrame([[1, Number_of_topping]], columns=['size', 'number of topping'])

elif "large" in size:
    order = pd.DataFrame([[2, Number_of_topping]], columns=['size', 'number of topping'])

else:
    print(f"Sorry, but we don't have {size} size pizza")

# Predicting and Printing Price
price = model.predict(order)
print("+","-"*65,"+")

print(f"+ Price: {price} +".center(50))
print("+","-" * 65,"+")
