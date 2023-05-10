# CTI-110
# P3HW2 - Salary
# Nicolette Johnson
# 08 April 2023


#pseudocode
# name = input 
# display "Enter employee's name:""
# hours = input
# display "Enter number of hours worked: "
# pay = input
# display "Enter employee's pay rate: "
# overtime_hours = input
# if hours > 40
#    then overtime_hours = hours - 40
# overtime_pay = pay * overtime_hours
# reghour_pay = pay * hours
# grossPay = reghour_pay + overtime_pay
# display "Employee name:", name
# display "Hours Worked    Pay Rate   OverTime    OverTime Pay    RegHour Pay    Gross Pay"
# display hours, pay, overtime_hours, overtime_pay, reghour_pay, grospay




# user input
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))


overtime_hours = int()
if hours > 40:
  overtime_hours = hours - 40

# equations
overtime_pay = pay * overtime_hours
reghour_pay = pay * hours
grossPay = reghour_pay + overtime_pay

#results
print("----------------------------------")
print("Employee name:", (name))
print("Hours Worked    Pay Rate   OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")
print(f'{hours:<15.2f}{pay:<10.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{reghour_pay:<15.2f}{grossPay:<15.2f}')