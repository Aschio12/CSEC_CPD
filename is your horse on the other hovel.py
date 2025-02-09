a =list(map(int,input().split()))
b=list(set(a))
counts = [a.count(item) for item in b]
ans=0
for i in (counts):
    if i>1:
        ans+=i-1
print(ans)
