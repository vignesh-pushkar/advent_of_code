a= []
b=[]
while(True):
    st = input()
    if(not st):
        break
    if(len(st.split("-"))<2):
        b.append(st)
    else:
        a.append(st.split("-"))
ct=0
print(a, b)
for i in b:
    for j in a:
        if(int(j[0])<=int(i) and int(i) <= int(j[1])):
            ct+=1
            break
print(ct)
