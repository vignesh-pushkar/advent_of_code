arr=[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st.split(","))

arr = [(int(x), int(y)) for x, y in arr]
mar=0
for i in arr:
    for j in arr:
        area=abs(i[0]-j[0]+1)*abs(i[1]-j[1]+1)
        mar=max(area, mar)
print(mar)
