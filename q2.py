import itertools

a=input()
ss=set()
m=-1
for i in a:
    if i.isdigit():
       ss.add(i)

ll=list(itertools.permutations(ss,len(ss)))
print(ll)
for i in ll:
    k="".join(i)
    if int(k)%2==0 and int(k)>m:
        m=int(k)
print(m)
