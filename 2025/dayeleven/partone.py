arr=[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st.split())


for i in arr:
    i[0]=i[0][:3]

car=[]
def counter(ind):
    if 'out' in arr[ind][1:]:
        return 1
    ct=0
    for i in arr[ind][1:]:
        for j in arr:
            if(i==j[0]):
                ct+= counter(arr.index(j))
    return ct

for i in arr:
    if(i[0]=="you"):
        out=counter(arr.index(i))
        break

print(out)
