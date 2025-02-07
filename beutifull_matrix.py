matrix=[]
for i in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col]==1:
            posx=row
            posy=col
            break
print(abs(2-posx)+abs(2-posy))

