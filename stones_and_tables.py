num=int(input())
color=input()
count=0
for i in range(1,num):
    if color[i]==color[i-1]:
        count+=1
print(count)
