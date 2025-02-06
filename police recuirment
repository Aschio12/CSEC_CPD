event = int(input())
occurenc_event = list(map(int, input().split()))
count = 0
numPolice = 0

for i in range(event):
    if occurenc_event[i] > 0:
        numPolice += occurenc_event[i]
    elif occurenc_event[i] == -1:
        if numPolice > 0:
            numPolice -= 1
        else:
            count += 1

print(count)
