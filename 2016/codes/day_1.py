# --- Day 1: No Time for a Taxicab ---
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

# For example:

# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?
import math

def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        splited_content = content[0].split(", ")
        direction = ['N','E','S','W']
        cur_dir = 0
        x = 0
        y = 0

        for i in splited_content:
            if i[0] == 'R':
                cur_dir = (cur_dir + 1) % 4
            else:
                if cur_dir - 1 < 0:
                    cur_dir = len(direction) - 1
                else:
                    cur_dir = (cur_dir - 1)
            

            steps = int(i[1:])

            if direction[cur_dir] == 'N':
                x+=steps
            elif direction[cur_dir] == 'E':
                y+=steps
            elif direction[cur_dir] == 'S':
                x-=steps
            else:
                y-=steps        

        return abs(x) + abs(y)
# --- Part Two ---
# Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

# How many blocks away is the first location you visit twice?


def question2(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        splited_content = content[0].split(", ")
        direction = ['N','E','S','W']
        cur_dir = 0
        x = 0
        y = 0
        dict_used_path = {}
        for i in splited_content:
            if i[0] == 'R':
                cur_dir = (cur_dir + 1) % 4
            else:
                if cur_dir - 1 < 0:
                    cur_dir = len(direction) - 1
                else:
                    cur_dir = (cur_dir - 1)
            

            steps = int(i[1:])

            if direction[cur_dir] == 'N':
                for i in range(steps):
                    x+=1
                    string_pos = str(x)+','+str(y)
                    if string_pos in dict_used_path:
                        return abs(x) + abs(y)
                    else:
                        dict_used_path[string_pos] = 1
            elif direction[cur_dir] == 'E':
                for i in range(steps):
                    y+=1
                    string_pos = str(x)+','+str(y)
                    if string_pos in dict_used_path:
                        return abs(x) + abs(y)
                    else:
                        dict_used_path[string_pos] = 1
            elif direction[cur_dir] == 'S':
                for i in range(steps):
                    x-=1
                    string_pos = str(x)+','+str(y)
                    if string_pos in dict_used_path:
                        return abs(x) + abs(y)
                    else:
                        dict_used_path[string_pos] = 1
            else:
                for i in range(steps):
                    y-=1
                    string_pos = str(x)+','+str(y)
                    if string_pos in dict_used_path:
                        return abs(x) + abs(y)
                    else:
                        dict_used_path[string_pos] = 1        

        return abs(x) + abs(y)

# print(question2('../files/test.txt'))

print(question1('../files/day1_input.txt'))
print(question2('../files/day1_input.txt'))
