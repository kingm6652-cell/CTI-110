# Maria King
# 10/12/25
# P2HW1
# Change formating of program P1HW2



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
print(f"\n ---------Travel Expenses-------")
print(f"Gas:           ${gas:.2f}")
print(f"Accommodation:  ${accommodation:.2f}")
print(f"Food:           ${food:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"-------------------------------")
print(f"Remaining Balance: ${remaining:.2f}")
