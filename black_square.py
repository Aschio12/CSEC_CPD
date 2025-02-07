strip_calories=list(map(int,input().split(" ")))
square_on_strip=list(map(int,input()))
calorie=0
for i in (square_on_strip):
    calorie+=strip_calories[i-1]
print(calorie)
