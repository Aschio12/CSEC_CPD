prize,r=map(int,input().split())
shovel=1
while True:
    if (prize *shovel)%10==0 or (prize *shovel)%10==r:
        break
    else:
        shovel+=1
print(shovel)
