########################################################
#
#    Treasure Map (by AnggiBK)
#    
#    One Exercise Topic of "Day 4" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column_pos = int(position[0])
row_pos = int(position[1])

map[row_pos-1][column_pos-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")