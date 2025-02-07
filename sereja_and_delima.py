n=int(input())
arr=list(map(int,input().split(" ")))
left, right = 0, n - 1
sereja_score, dima_score = 0, 0
turn = 0  

while left <= right:
    if arr[left] > arr[right]:
        current_pick = arr[left]
        left += 1
    else:
        current_pick = arr[right]
        right -= 1

    if turn == 0:
        sereja_score += current_pick
    else:
        dima_score += current_pick

    turn = 1 - turn  

print( sereja_score, dima_score)

