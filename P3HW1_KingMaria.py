 # Maria King
 # 10/26/25
 # P3HW1
 # Debug the program below


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [int(mod_1), int(mod_2), int(mod_3), int(mod_4), int(mod_5), int(mod_6)]

print("\n------------Results------------")
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)
print("\n------------------------------")
# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
else:
print('Your grade is: F') # TO DO: finish this


