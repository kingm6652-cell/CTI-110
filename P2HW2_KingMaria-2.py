# P2HW2_KingMaria.py
# Maria King
# Date: 0/12/2025
# Description: Design a prgrom that shows the grade of tests scores. 

# Pseudocode (Algorithm):
# 1. Create an empty list to store grades.
# 2. Prompt the user to enter a grade for Module 1 and add it to the list.
# 3. Prompt the user to enter a grade for Module 2 and add it to the list.
# 4. Prompt the user to enter a grade for Module 3 and add it to the list.
# 5. Prompt the user to enter a grade for Module 4 and add it to the list.
# 6. Prompt the user to enter a grade for Module 5 and add it to the list.
# 7. Prompt the user to enter a grade for Module 6 and add it to the list.
# 8. Calculate the lowest grade in the list.
# 9. Calculate the highest grade in the list.
# 10. Calculate the sum of all grades in the list.
# 11. Calculate the average of the grades (sum divided by number of grades).
# 12. Display the results in a formatted output block.

# Add your code below
grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

print("\n------------Results------------")
print(f"Lowest Grade:      {min(grades):.2f}")
print(f"Highest Grade:     {max(grades):.2f}")
print(f"Sum of Grades:     {sum(grades):.2f}")
print(f"Average:           {sum(grades)/len(grades):.2f}")
print("------------------------------")

