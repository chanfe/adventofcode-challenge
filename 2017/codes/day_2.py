# --- Day 2: Corruption Checksum ---
# As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

# The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

# For example, given the following spreadsheet:

# 5 1 9 5
# 7 5 3
# 2 4 6 8
# The first row's largest and smallest values are 9 and 1, and their difference is 8.
# The second row's largest and smallest values are 7 and 3, and their difference is 4.
# The third row's difference is 6.
# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

# What is the checksum for the spreadsheet in your puzzle input?

import math

def question1(file):
    with open(file) as f:
        answer = 0
        content = f.readlines()
        content = [x.strip() for x in content]
        for row in content:
            splited_row = row.split("\t")
            biggest = 0
            smallest = int(splited_row[0])
            for i in splited_row:
                if int(i) > biggest:
                    biggest = int(i)
                if int(i) < smallest:
                    smallest = int(i)
            answer += biggest - smallest
        return answer

# --- Part Two ---
# "Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

# "Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

# It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

# For example, given the following spreadsheet:

# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
# In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
# In the second row, the two numbers are 9 and 3; the result is 3.
# In the third row, the result is 2.
# In this example, the sum of the results would be 4 + 3 + 2 = 9.

# What is the sum of each row's result in your puzzle input?

def question2(file):
    with open(file) as f:
        answer = 0
        content = f.readlines()
        content = [x.strip() for x in content]
        for row in content:
            splited_row = row.split()
            for i in range(len(splited_row)):
                for j in range(len(splited_row)):
                    if i == j:
                        continue
                    if float(splited_row[i]) % float(splited_row[j]) == 0:
                        answer += int(splited_row[i]) / int(splited_row[j])

        return answer

# print(question2('../files/test.txt'))
print(question1('../files/day2_input.txt'))
print(question2('../files/day2_input.txt'))      
