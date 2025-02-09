stone_pos=input()
instruction=input()
pos=0
for i in range(len(instruction)):
    if instruction[i]==stone_pos[pos]:
        pos+=1
print(pos+1)
