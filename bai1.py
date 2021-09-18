list = [2,6,8,1,4,7]
B=len(list)
for i in range(0,B-1):
    for j in range(i+1,B):
        if(list[i]>list[j]):
            A=list[i]
            list[i]=list[j]
            list[j]=A
print(list)