n = int(input())
teams = []
for _ in range(n):
    hi, ai = map(int, input().split())
    teams.append([hi, ai])
count = 0

for i in range(n):  
    host_home = teams[i][0]
    for j in range(n):
        away_team=teams[j][1]
        if host_home==away_team:
            count+=1

print(count)
