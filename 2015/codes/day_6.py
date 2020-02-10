# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?
import math
import re


def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        grid = []
        for i in range(1000):
            grid.append([0] * 1000)
        for i in content:
            coordinate = re.findall('\d{1,3},\d{1,3}', i)
            key_word = re.search('(on|off|toggle)', i)
            x1,y1 = coordinate[0].split(',')
            x2,y2 = coordinate[1].split(',')
            x1 = int(x1)
            x2 = int(x2) +1
            y1 = int(y1)
            y2 = int(y2) +1

            if key_word.group() == 'on':
                for i in range(y1,y2):
                    for j in range(x1,x2):
                        grid[i][j] = 1
            elif key_word.group() == 'off':
                for i in range(y1,y2):
                    for j in range(x1,x2):
                        grid[i][j] = 0
            else:
                for i in range(y1,y2):
                    for j in range(x1,x2):
                        grid[i][j] = 1 - grid[i][j]
        total = 0
        for i in range(1000):
            for j in range(1000):
                if grid[i][j] == 1:
                    total += 1
        return total

# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

def question2(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        grid = []
        for i in range(1000):
            grid.append([0] * 1000)
        for i in content:
            coordinate = re.findall('\d{1,3},\d{1,3}', i)
            key_word = re.search('(on|off|toggle)', i)
            x1,y1 = coordinate[0].split(',')
            x2,y2 = coordinate[1].split(',')
            x1 = int(x1)
            x2 = int(x2) +1
            y1 = int(y1)
            y2 = int(y2) +1

            if key_word.group() == 'on':
                for i in range(y1,y2):
                    for j in range(x1,x2):
                        grid[i][j] += 1
            elif key_word.group() == 'off':
                for i in range(y1,y2):
                    for j in range(x1,x2):
                        temp = grid[i][j] - 1
                        if temp < 0:
                            grid[i][j] = 0
                        else:
                            grid[i][j] = temp
                        
            else:
                for i in range(y1,y2):
                    for j in range(x1,x2):
                        grid[i][j] += 2
        total = 0
        for i in range(1000):
            for j in range(1000):
                total += grid[i][j]
        return total


print(question1('../files/day6_input.txt'))
print(question2('../files/day6_input.txt'))
