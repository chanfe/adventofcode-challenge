def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        answer = 0
        for i in content:
            answer += int(i)
        print (answer)

def question2(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        dict = {}
        answer = 0;
        i = 0
        while True:
            answer += int(content[int(i) % len(content)])
            if answer in dict:
                return answer
            else:
                dict[answer] = "hi"
            i += 1

print(question1('../files/test.txt'))
print(question1('../files/day2_input.txt'))
print(question2('../files/test.txt'))
print(question2('../files/day2_input.txt'))
