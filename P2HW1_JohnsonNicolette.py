# Travel Expense Calculator
# 08 April 2023
# CTI-110 P2HW1 - Travel Expense
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


# add float in front of all inputs


# remaining_balance = budget - (gas + hotel + food)
# display "----Travel Expenses----"
# display "Location: " + destination
# display "Initial Budget: $" + budget
# display "fuel: $" + gas
# display "Accomodation: $" + hotel
# display "Food: $" + food
# display "-----------------------"
# display "Remaining Balance: $" + remaining_balance

print("This program calculates and displays travel expenses.")

budget = float(input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remaining_balance = float(budget - (gas + hotel + food))

print("------------Travel Expenses------------")
print(f'Location:         {destination}')
print(f'Initial Budget:   ${budget}')
print(f'Fuel:             ${gas}')
print(f'Accomodation:     ${hotel}')
print(f'Food              ${food}')
print("---------------------------------------")

print(f'Remaining Balance ${remaining_balance}')

