weight=(input()).split(" ")
limak=int(weight[0])
bob=int(weight[1])
count=0
while(limak<=bob):
    limak*=3
    bob*=2
    count+=1
print(count)
