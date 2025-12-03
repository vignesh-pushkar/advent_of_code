arr=[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st)
print(arr)
add=0
for i in arr:
    a=max(i)
    
    if(i.index(a)==len(i)-1):
        b=a
        a=max(i[0:len(i)-1])
    else:
        b=max(i[i.index(a)+1:])
    add += int(a)*10+int(b)
    print(a, b)
print(add)
