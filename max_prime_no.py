n = int(input())
temp = 2
buff = n
while(temp<n): 
    if(buff<temp):
        break
    if (buff%temp == 0):
        #print(temp)
        buff=int(buff/temp)
    temp = temp+1 
print(temp-1)
