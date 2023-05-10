# Travel Expense Calculator
# 08 April 2023
# CTI-110 P1HW1 - Travel Expense
# Nicolette Johnson

# pseudocode
# display "this program calculates and displays travel expenses."
# display "enter budget"
# input budget
# display "Enter your travel destination: "
# input travel destination
# display "How much do you think you will spend on gas? $"
# input gas
# display ""Approximately, how much will you need for accomodation/hotel? $"
# input hotel
# display "Last, how much do you need for food? $"
# input food

# remaining_balance = budget - (gas + hotel + food)
# display "----Travel Expenses----"
# display "Location: " + destination
# display "Initial Budget: $" + budget
# display "fuel: $" + gas
# display "Accomodation: $" + hotel
# display "Food: $" + food
# display "Remaining Balance: " + remaining_balance

print("This program calculates and displays travel expenses.")

budget = int(input("Enter budget: $"))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? $"))
hotel = int(input("Approximately, how much will you need for accomodation/hotel? $"))
food = int(input("Last, how much do you need for food? $"))

remaining_balance = budget - (gas + hotel + food)

print("----Travel Expenses----")
print("Location: ",(destination))
print("Initial Budget: $",(budget))
print("Fuel: $",(gas))
print("Accomodation: $",(hotel))
print("Food: $",(food))
print("Remaining Balance: "(remaining_balance))

