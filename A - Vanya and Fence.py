fnum_height=input().split(" ")
fheight=list(map(int,input().split()))
len_road=0
h=int(fnum_height[1])
for i in range(len(fheight)):
    if fheight[i]>h:
        len_road+=2
    else:
        len_road+=1
print(len_road)
