# Maria King
# 9/28/25
# P1HW2
# Description: Create a program that does Math Calculations

"""
Pseudocode (Program Logic):
1. Display a message about the program's purpose.
2. Ask the user to enter their budget and store the value.
3. Ask the user to enter their travel destination and store the value.
4. Ask the user for the amount they will spend on gas and store the value.
5. Ask the user for the amount they will spend on accommodation and store the value.
6. Ask the user for the amount they will spend on food and store the value.
7. Add up the expenses (gas, accommodation, food) to get the total expenses.
8. Subtract the total expenses from the budget to get the remaining balance.
9. Display the travel destination, initial budget, each expense, total expenses, and remaining balance.
"""


print(" This program calculates and displays travel expenses")

# Ask user to enter their budget
budget = float(input("Enter your budget: $"))

# Ask user to enter travel destination

destination = input("Enter your travel destination: ")


# Ask user for amount they will spend on gas

gas = float(input("Enter amount you will spend on gas: $"))


# Ask user for amount they will spend on accommodation

accommodation = float(input("Enter amount you will spend on accommodation: $"))


# Ask user for amount they will spend on food

food = float(input("Enter amount you will spend on food: $"))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget
remaining = budget - total_expenses

# Display results
print()
print("Travel Destination:", destination)
print(f"Initial Budget: ${budget:.2f}")
print(f"\nExpenses:")
print(f"Gas:           ${gas:.2f}")
print(f"Accommodation:  ${accommodation:.2f}")
print(f"Food:           ${food:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"\nRemaining Balance: ${remaining:.2f}")


