# Travel Expense Calculator
# 08 April 2023
# CTI-110 P2HW1 - Travel Expense
# Nicolette Johnson

# pseudocode
# display module1
# module1 = input
# display module2
# module2 = input
# display module3
# module3 = input
# display module4
# module4 = input
# display module5
# module5 = input
# display module6
# module6 = input

# lowGrade = min(all  modules)
# highGrade = max(all  modules)
# sum = module1 + module2 + module3 + module4 + module5 + module6
# average = sum/6

# display "--------Results--------"
# display "Lowest Grade: "  + lowGrade
# display "Highest Grade: " + highGrade
# display "sum of grades: " + sum
# display "Average: "       + average
# display "-----------------------"

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

lowGrade = min(module1, module2, module3, module4, module5, module6)
highGrade = max(module1, module2, module3, module4, module5, module6)
sum = module1 + module2 + module3 + module4 + module5 + module6
average = sum/6

print("----------------Results----------------")
print(f'Lowest Grade:     {lowGrade}')
print(f'Highest Grade:    {highGrade}')
print(f'Sum of Grades:    {sum}')
print(f'Average:          {average}')
print("---------------------------------------")


