arr=[]
while(True):
    st=input()
    if(not st):
        break
    arr.append([int(x) for x in st.split(",")])

def dist(x, y):
    return ((x[0]-y[0])**2)+((x[1]-y[1])**2)+((x[2]-y[2])**2)

wts=[]

for i in arr:
    line=[]
    for j in arr:
        line.append(dist(i, j))
    wts.append(line)

mwt=float('inf')
for line in wts:
        for val in line:
            if(val!=0):
                mwt=min(mwt, val)



wst=set()
for i in wts:
    for j in i:
        wst.add(j)
wst.remove(0)
wlt=[]
'''
wlt=list(wst)
wlt.sort()
print(mwt)
'''
for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        if(dist(arr[i], arr[j])!=0):
            wlt.append([dist(arr[i], arr[j]), i, j])
wlt.sort(key=lambda x:x[0])
n=1000

ars=[]
for i in range(0, len(arr)):
    ars.append([arr[i], i, 1])

def union(x, y):
    k=x
    while(ars[k][1]!=k):
        k=ars[k][1]
    l=y
    while(ars[l][1]!=l):
        l=ars[l][1]
    
    if(k==l):
        return
    x=k
    y=l
    
    if(ars[x][2]>ars[y][2]):
        i, j=x, y
    else:
        j, i=x, y
    ars[j][1]=i
    ars[i][2]+=ars[j][2]
    ars[j][2]=0

for j in range(0, n):
    union(wlt[j][1], wlt[j][2])

slt=[]
for i in ars:
    slt.append(i[2])
    
slt.sort(reverse=True)

print(slt[0], "x", slt[1], "x", slt[2], "=", slt[0]*slt[1]*slt[2])
