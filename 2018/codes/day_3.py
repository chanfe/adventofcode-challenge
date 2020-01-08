def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        answer = 0
        dic = {}
        two_true = False
        three_true = False
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
                    two_true = True
                elif dic[x] == 3:
                    three_true = True

            if two_true == True:
                all_two += 1
                two_true = False

            if three_true == True:
                all_three += 1
                three_true = False

            dic = {}

        print (all_two * all_three)

def question2(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        answer = ""
        answer2 = ""
        test_answer = ""
        real_answer = ""
        main_string = ""
        dif_conter = 0
        for i in range(len(content)): #first loop
            main_string = content[i]
            for j in range(i+1, len(content)): #second loop
                for x in range(len(content[i])): # foor loop for the indivdial char
                    if main_string[x] != content[j][x]:
                        dif_conter += 1
                    else:
                        test_answer += main_string[x]
                if dif_conter == 1:
                    answer = main_string
                    answer2 = content[j]
                    real_answer = test_answer
                    break
                test_answer = ""
                dif_conter = 0
        print(answer, answer2, real_answer)






print(question2('../files/day2_input.txt'))
