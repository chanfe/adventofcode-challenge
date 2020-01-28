# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?

def question1(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        naughty_str = ["ab", "cd", "pq", "xy"]
        vowels = ['a','e','i','o','u']
        not_naughty = True
        num_of_vowels = 0
        duplicate = False 
        nice = 0
        for i in content:
            for j in range(len(i)):
                if i[j] in vowels:
                    num_of_vowels += 1
                try:
                    if i[j] == i[j+1]:
                        duplicate = True
                    holder = i[j] + i[j+1]
                    if holder in  naughty_str:
                        not_naughty = False
                        break
                except:
                    pass
                
                
            if num_of_vowels >= 3 and duplicate and not_naughty:
                nice += 1
            num_of_vowels = 0
            duplicate = False
            not_naughty = True
        return nice 
            
# --- Part Two ---
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?

def question2(file):
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        
        pairs = False
        inbetween = False
        nice = 0
        for i in content:
            dic = {}
            for j in range(len(i)):
                try:
                    if i[j] == i[j+2]:
                        inbetween = True
                except:
                    pass
                try:
                    holder = i[j] + i[j+1]
                    if holder in dic:
                        if j - dic[holder] > 1:
                           pairs = True 
                    else:
                        dic[holder] = j
                except:
                    pass
                
            if pairs and inbetween:
                nice += 1
            pairs = False
            inbetween = False
        return nice 

print(question1('../files/day5_input.txt'))
print(question2('../files/day5_input.txt'))