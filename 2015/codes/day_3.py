# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
import math

def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        total = 1
        table_dic = {}
        x = 0
        y = 0
        for i in content:
            position = str(x) + '-' + str(y)
            table_dic[position] = 1
            for j in i:
                if(j == '^'):
                    y+=1
                if(j == '>'):
                    x+=1
                if(j == '<'):
                    x-=1
                if(j == 'v'):
                    y-=1
                position = str(x) + '-' + str(y)
                try:
                    table_dic[position]
                    table_dic[position] = table_dic[position] + 1
                except:
                    table_dic[position] = 1
                    total += 1
            return total
                

# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

def question2(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        total = 1
        table_dic = {}
        x = 0
        y = 0
        rx = 0
        ry = 0
        for i in content:
            position = str(x) + '-' + str(y)
            table_dic[position] = 2
            counter = 0
            for j in i:
                if(j == '^'):
                    if(counter % 2 == 1):
                        ry += 1
                    else:
                        y+=1
                if(j == '>'):
                    if(counter % 2 == 1):
                        rx += 1
                    else:
                        x+=1
                if(j == '<'):
                    if(counter % 2 == 1):
                        rx -= 1
                    else:
                        x-=1
                if(j == 'v'):
                    if(counter % 2 == 1):
                        ry -= 1
                    else:
                        y-=1
                position = str(x) + '-' + str(y)
                if(counter % 2 == 1):
                    position = str(rx) + '-' + str(ry)
                try:
                    table_dic[position]
                    table_dic[position] = table_dic[position] + 1
                except:
                    table_dic[position] = 1
                    total += 1
                counter += 1
            return total

print(question1('../files/day3_input.txt'))
print(question2('../files/day3_input.txt'))