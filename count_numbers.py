#!/usr/bin/env python3

numberDict = { 
        0 : "zero",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety"
        }


def numbers(num):
    letters = ""
    if 0 < num <= 20:
        letters += numberDict[num]
    elif 21 < num <= 99:
        val_1 = num%10 # 85%10 = 5
        val_2 = (int(num/10))*10 # 85/10 = 8*10
        letters += numberDict[val_1]+numberDict[val_2]
    else:
        if 100 < num <= 120:
            letters += numberDict[num/100]+ "hundredand" + numberDict[num%100]
        else:
            #val_3 = num%10 #135%10 = 5
            val_4 = (int((num%100)/10))*10 # (int((998%100)/10))*10
            letters += numberDict[int(num/100)]+"hundredand"+numberDict[val_4]+numberDict[num%10]
    count = len(letters)
    return count

sum=0
for i in range(1,101):
    sum+= numbers(i)
    
print("sum "+str(sum))
