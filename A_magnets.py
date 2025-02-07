num=int(input())
pre=""
count=0
for i in range(num):
    currentPole=input()
    if currentPole!=pre:
        count+=1
    pre=currentPole
print(count)
