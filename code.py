# Simple budget calculator  V1.0
# Written by : Alejandro Becerra

# This small python script will help you calculate a financially healthy
# distribution for your income, providing information for your monthly budget

# variables
monthly_rent_percentage = 0.3
monthly_savings_percentage = 0.1
monthly_living_expenses_percentage = 0.2
monthly_utilities_expenses_percentage = 0.2
monthly_leisure_expenses_percentage = 0.2
# list for operations
pct = ["monthly_rent_percentage", "monthly_savings_percentage", "monthly_living_expenses_percentage",
       "monthly_utilities_expenses_percentage ", "monthly_leisure_expenses_percentage"]

print("Hi! Welcome to your budget calculator.")
# user_name= str(input("What's your name? "))
# print("Cool "+ name)
print('We are going to help you manage your finances better.')
budget = float(input("What's your monthly income? "))
print("""Excellent. The recommended proportion to be spend in different areas of life ensuring you maintain
good financial health are 30% for rent, 10% for savings, 20% for groceries, 20% percent for utilities and 20% for 
leisure.""")
print("Thus the recommended distribution for your monthly budget is:")3
print("For rent: ")
print(budget * monthly_rent_percentage)
print("For savings: ")
print(budget*monthly_savings_percentage)
print("For groceries: ")
print(budget*monthly_living_expenses_percentage)
print("For utilities: ")
print(budget*monthly_utilities_expenses_percentage)
print("For leisure: ")
print(budget*monthly_leisure_expenses_percentage)
print("----")
print("Thank you for using our program! See you next month.")
