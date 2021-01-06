
import math

def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]

# print(question1('../files/test.txt'))
# print(question2('../files/test.txt'))
# print(question1('../files/day12_input.txt'))
# print(question2('../files/day12_input.txt'))