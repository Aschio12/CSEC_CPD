string=input()
currentpos=0
distance=0
for i in range(len(string)):
    target=ord(string[i])-ord("a")
    clockDistance=(target-currentpos)%26
    counterDistance=(currentpos-target)%26
    distance+=(min(clockDistance,counterDistance))
    currentpos=target
print(distance)
