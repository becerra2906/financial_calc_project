# Simple budget calculator  V1.01
# Written by : Alejandro Becerra 
#This small python script will help you calculate a financially healthy
#distribution for your income, providing information for your monthly budget

# V1.01 release notes: refactor the code to use format function for printing the output result and include the user input variable of name to provide a personalised experience

# pctg for calcs

monthly_rent_percentage = 0.3
monthly_savings_percentage = 0.1 
monthly_living_expenses_percentage = 0.2 
monthly_utilities_expenses_percentage = 0.2
monthly_leisure_expenses_percentage = 0.2 

# welcome user and get name

print("Hi! Welcome to your budget calculator. We are here to help you better allocate your monthly income, so you can save, invest and not overspend.")

# saves name variable to be used in the output description of the budget distribution 

name = input("What's your name?")

#
