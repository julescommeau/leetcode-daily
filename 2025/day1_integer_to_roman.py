def intToRoman(num: int) -> str:
    d = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), \
        ("M", 1000)]
    roman = ""
    while num >= d[-1][1]:
        roman += d[-1][0]
        num -= d[-1][1]
    # while num != 0:
    while num != 0:
        for i in range(2,-1,-1):
            if num == 0:
                break
                
            if num >= 10 ** i:
                p_chiffre = num // 10**i
                if p_chiffre == 9:
                    roman +=  d[-7 + i*2][0] + d[-5 + i*2][0]
                    num -=  d[-5 + i*2][1] - d[-7 + i*2][1]
                elif p_chiffre == 4:
                    roman += d[-7 + i*2][0] + d[-6 + i*2][0]
                    num -= d[-6 + i*2][1] - d[-7 + i*2][1]
                else:
                    while num >= 10 ** i:
                        if num >= 5 * 10 ** i:
                            roman += d[-6 + i*2][0]
                            num -= d[-6 + i*2][1]
                        else:
                            roman += d[-7 + i*2][0]
                            num -= d[-7 + i*2][1]
                        
                
    return roman

print(intToRoman(1))
print(intToRoman(2347))
print(intToRoman(3999))
print(intToRoman(2024))
print(intToRoman(1984))
print(intToRoman(999))
print(intToRoman(944))
print(intToRoman(900))
print(intToRoman(490))
print(intToRoman(17))