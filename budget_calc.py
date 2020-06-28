# Simple budget calculator  V1.02
# Written by : Alejandro Becerra 
#This small python script will help you calculate a financially healthy
#distribution for your income, providing information for your monthly budget

# V1.01 release notes: refactor the code to use format function for printing the output result and include the user input variable of name to provide a personalised experience
# V1.02 release notes: adds feedback loop to provide insights of over spending or buffers that coulb be used or redistributed



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

# if function to ask user if they want to compare their actual spending with the proposed distro

comparison = (input("Do you want to see how your spending compares to the proposed distribution? "))

affirmative = {"Yes", "yes", "YES", "sure", "Y", "y"}

#### negative = {"no", "No", "n", "N"} replaced with comparison not in affirmative to allow better response flexibility 


if comparison in affirmative: 


# V1.02 review and comparison of actual expenditure against proposed budgetary distribution

# actual expenditure (rent, savings, living expenses, utilities, leisure)


            actual_rent = int(input("How much do you currently pay in rent? "))
            actual_savings = int(input("How much are you currently saving? "))
            actual_expenses = int(input("How much do you currently spend on your living expenses? "))
            actual_utilities = int(input("How much do you currently pay in utility bills? "))
            actual_leisure = int(input("How much do you currently spend for leisure and entretainment? "))

            overrent = (actual_rent > rent)
            underrent = (actual_rent < rent)
            proprent = (actual_rent == rent)
            
            if overrent == True: 
                                print("You're spending more on rent than you should.")
            if underrent == True:
                                print("You're spending less on rent than you could.")
            if proprent == True: 
                                print("You're spending on rent what you should.")

            oversave = (actual_savings > savings)
            undersave = (actual_savings < savings)
            propsave = (actual_savings == savings)
            
            if oversave == True: 
                                print("You're saving more than you should.")
            if undersave == True:
                                print("You're saving less than you could.")
            if propsave == True: 
                                print("You're saving what you should.")
            
            overexpenses = (actual_expenses > expenses)
            underexpenses = (actual_expenses < expenses)
            propexpenses = (actual_savings == savings)
            
            if overexpenses == True: 
                                print("You're spending more on your living expenses than you should.")
            if underexpenses == True:
                                print("You're spending less on your living expenses than you could.")
            if propexpenses == True: 
                                print("You're spending on your living expenses what you should.")
                            
            overutilities = (actual_utilities > utilities)
            underutilities = (actual_utilities < utilities)
            proputilities = (actual_utilities == utilities)
            
            if overutilities == True: 
                                print("You're spending more on your utilities than you should.")
            if underutilities == True:
                                print("You're spending less on your utilities than you could.")
            if proputilities == True: 
                                print("You're spending on your utilities what you should.")

                                
            overleisure = (actual_leisure > leisure)
            underleisure = (actual_leisure < leisure)
            propleisure = (actual_leisure == leisure)
            
            if overleisure == True: 
                                print("You're spending more on your leisure than you should.")
            if underleisure == True:
                                print("You're spending less on your leisure than you could.")
            if propleisure == True: 
                                print("You're spending on your leisure what you should.")

            print("---------------")
            print("Thank you for using the budget calculator! I hope it was useful!")

if comparison not in affirmative:                    
    print("---------------")
    print("Thank you for using the budget calculator! I hope it was useful!")
