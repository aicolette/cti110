# CTI-110
# P4HW1 - Score List
# Nicolette Johnson
# 27 April 2023


# pseudocode
# Declare Real score_list, score_num, score
# when 1 < i < score_num
  # if score is between 0 and 100
  # display 'How many scores do you want to enter?'
  # user input score
    # score added to database
  #else 
    # display "IVALID Score entered!!!!"
    # display "Score should be between 0 and 100"
    # ask user to reenter valid score 
    # add new score to database
# Display lowest score and find min
# remove min from score_list
# modify score_num = score_num - 1
# Display modified score_list
# Display score_list average
# Declare grade real 
# if averaGe >= 90 
  # grade = A
# else if average >= 80 
  # grade = B
# else if average >= 70 
  # grade = C
# else if average >= 60 
  # grade = D
# else
  # grade = F
# Display grade 

score = []
score_list = []
score_num = int(input('How many scores do you want to enter? '))

print("\n")

for i in range(score_num):
    score = int(input("Enter score #{} : ".format(i+1)))
    while True:
                if 0 <= score <= 100:
                        break
                score = int(input("INVALID Score enter!!!!\n" "Score Should be between 0 and 100\n" "Enter score #{} again: ".format(i + 1)))
    score_list.append(score)

print('\n')


print("----------------Results----------------")
print("Lowest Score: {}".format(min(score_list)))

score_list.remove(min(score_list))
score_num = score_num - 1

print(f'Modified List: {score_list}')
print("Score's Average: {}".format(sum(score_list)/(score_num)))

grade = []
if sum(score_list)/(score_num) >= 90:
        grade = "A"
elif sum(score_list)/(score_num) >= 80:
        grade = "B"
elif sum(score_list)/(score_num) >= 70:
        grade = "C"
elif sum(score_list)/(score_num) >= 60:
        grade = "D"
else:
        grade = "F"
      
print(f'Grade: {grade}')
print("---------------------------------------")

