# Runtime : 0ms (Beats 100%)
# Memory : 12.42 MB (Beats  52.43%)

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    letters = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    lst_comb = list()
    if len(digits) == 1:
        for i in range(len(letters[int(digits[0])-2])):
            lst_comb.append(letters[(int(digits[0])-2)][i])
    elif len(digits) == 2:
        for i in range(len(letters[int(digits[0])-2])):
            for j in range(len(letters[int(digits[1])-2])):
                lst_comb.append(letters[(int(digits[0])-2)][i] + \
                    letters[(int(digits[1])-2)][j])
    elif len(digits) == 3:
        for i in range(len(letters[int(digits[0])-2])):
            for j in range(len(letters[int(digits[1])-2])):
                for k in range(len(letters[int(digits[2])-2])):
                    lst_comb.append(letters[(int(digits[0])-2)][i] + \
                    letters[(int(digits[1])-2)][j] + \
                    letters[(int(digits[2])-2)][k])
                    
    elif len(digits) == 4:
        for i in range(len(letters[int(digits[0])-2])):
            for j in range(len(letters[int(digits[1])-2])):
                for k in range(len(letters[int(digits[2])-2])):
                    for l in range(len(letters[int(digits[3])-2])):
                        lst_comb.append(letters[(int(digits[0])-2)][i] + \
                        letters[(int(digits[1])-2)][j] + \
                        letters[(int(digits[2])-2)][k] + \
                        letters[(int(digits[3])-2)][l])

    return lst_comb
    
print(letterCombinations("5678"))
print(len(letterCombinations("567")))

for i in range(2,10):
    for j in range(2,10):
        for k in range(2,10):
            for l in range(2,10):
                letterCombinations(str(i)+str(j)+str(k)+str(k))