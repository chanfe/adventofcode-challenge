def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        answer = 0
        dic = {}
        all_two = 0
        all_three = 0
        for i in content:
            for j in i:
                if j in dic:
                    dic[j] = dic[j] + 1
                else:
                    dic[j] = 1

            for x in dic:
                if dic[x] == 2:
                    all_two += 1
                elif dic[x] == 3:
                    all_three += 1
            print (dic, all_two, all_three)
            dic = {}
        print (dic)
        print (all_two * all_three)

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
