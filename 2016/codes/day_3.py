# --- Day 3: Squares With Three Sides ---
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

# Or are they?

# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

# In your puzzle input, how many of the listed triangles are possible?

import math

def _valid_triangle(a,b,c):
    if a + b <= c:
        return False
    elif a + c <= b:
        return False
    elif b + c <= a:
        return False
    return True

def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        answer = 0
        for i in content:
            splited = i.split()
            if _valid_triangle(int(splited[0]), int(splited[1]), int(splited[2])):
                answer += 1
        return answer

# --- Part Two ---
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

# print(question1('../files/test.txt'))
# print(question2('../files/test.txt'))
# print(question1('../files/day3_input.txt'))
# print(question2('../files/day3_input.txt'))