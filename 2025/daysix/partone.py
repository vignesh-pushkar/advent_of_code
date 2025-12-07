arr =[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st.split())

opr = arr[len(arr)-1]
print(arr, opr)
out=0
for i in range(0, len(opr)):
    if(opr[i]=='+'):
        add=0
    else:
        add=1
    for j in range(0, len(arr)-1):
        if(opr[i]=='+'):
            add+=int(arr[j][i])
        else:
            add*=int(arr[j][i])
    out+=add
print(out)
