data=[]
while(True):
    st = input()
    if(not st):
        break
    data.append(st.split())
a=[]
b=[]
for i in data:
    a.append(int(i[0]))
    b.append(int(i[1]))
a.sort()
b.sort()
d = 0
sim=0
for i in a:
    ct=0
    for j in b:
        if(i==j):
            ct+=1
    sim+=ct*i        
print(sim)
