arr=[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st.split(","))

mx=(max([int(x[0]) for x in arr]))
my=(max([int(x[1]) for x in arr]))
print(mx, my)
dsp=[]

line=[]
for j in range(0, mx+1):
    line.append('.')
for i in range(0, my+1):
    dsp.append(line)

arr = [(int(x), int(y)) for x, y in arr]

for (x, y) in arr:
    dsp[y][x]='#'
    print(x, y)

print(dsp[0])
print(dsp[1])
for i in range(0, my+1):
    for j in range(0, mx+1):
        print(dsp[i][j], end="")
    print()
    



mar=0
for i in arr:
    for j in arr:
        area=abs(i[0]-j[0]+1)*abs(i[1]-j[1]+1)
        mar=max(area, mar)
print(mar)
