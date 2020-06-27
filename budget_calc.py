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

name = input("What is your name? ")

# saves the monthly income stated by the user as a variable. This income will
# be used to calculate a budget

income = float(input("What is your monthly income? "))

# calculate budgetary distro

rent = int(income * monthly_rent_percentage)

savings = int(income * monthly_savings_percentage)

expenses = int(income * monthly_living_expenses_percentage)

utilities = int(income * monthly_utilities_expenses_percentage)

leisure = int(income * monthly_leisure_expenses_percentage)

# print distro 

distro_message_="""{} based on your monthly budget you should save {}, you should use {} for paying rent, you should use {} for your monthly living expenses, you should use {} for paying your utilities and you should use {} for leisure expenses.""".format(name, str(savings), str(rent), str(expenses), str(utilities), str(leisure))

print(distro_message_)
print("---------------")
print("Thank you for using the budget calculator! I hope it was useful!")
