games=int(input())
wins=input().replace(" ","").upper()
if all(win in "AD" for win in wins)and games==len(wins):
    if wins.count("A")>wins.count("D"):
        print("Anton")
    elif wins.count("D")>wins.count("A"):
        print("Danik")
    else:
        print("Friendship")
