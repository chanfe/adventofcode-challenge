# --- Day 5: Binary Boarding ---
# You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

# You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

# Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

# For example, consider just the first seven characters of FBFBBFFRLR:

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

# Here are some other boarding passes:

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

import math

def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        row = 128
        col = 8
        answer = 0
        for i in content:
            row_inst = i[:-3]
            col_inst = i[-3:]
            r = partition(row_inst, row)
            c = partition(col_inst, col)
            a = ((r-1) * 8) + c-1
            if a > answer:
                answer = a
        return answer

def partition(instruction, max_num):
    l = 0
    u = max_num
    a = 0
    for i in instruction:
        if i == 'F' or i == 'L':
            u = (u+l)/2
            a = u
        elif i == 'B' or i == 'R':
            l = (u+l)/2
            a = l + 1
        else:
            return 'ERROR'
    return a

# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

# What is the ID of your seat?

# ID 95 - 838
def question2(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        row = 128
        col = 8
        find_dic = {}
        for i in range(95,838):
            find_dic[i] = 0
        for i in content:
            row_inst = i[:-3]
            col_inst = i[-3:]
            r = partition(row_inst, row)
            c = partition(col_inst, col)
            a = ((r-1) * 8) + c-1
            if a in find_dic:
                del find_dic[a]
        return find_dic

# print(question1('../files/test.txt'))
# print(question2('../files/test.txt'))
print(question1('../files/day5_input.txt'))
print(question2('../files/day5_input.txt'))