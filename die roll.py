yakko,wakko=map(int,input().replace(" ",""))
effective_die=7-max(yakko,wakko)
denomerater=6
ans=f"{int(effective_die)}/{int(denomerater)}"
temp=effective_die
while effective_die>0:
    if  denomerater%temp==0 and effective_die%temp==0:
        ans=f"{int(effective_die/temp)}/{int(denomerater/temp)}"
        break
    temp-=1      
print(ans)
