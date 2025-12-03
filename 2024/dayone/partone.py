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
for i, j in zip(a, b):
    d+=abs(i-j)
print(d)
