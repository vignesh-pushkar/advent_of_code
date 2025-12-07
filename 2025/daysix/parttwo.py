arr =[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st)

out=0
add=0

for j in range(0, len(arr[0])):
    if(arr[len(arr)-1][j]=='*'):
        out+=add
        add=1
        opr='*'
    elif(arr[len(arr)-1][j]=='+'):
        out+=add
        print(add, out, j)
        add=0
        opr='+'
        
    if(opr=='+'):
        num=0    
        for i in range(len(arr)-2, -1, -1):
            if(arr[i][j].isdigit()):
                num+=int(arr[i][j])*(10**len(str(num)))
        add+=int(num/10)   
    if(opr=='*'):
        num=0    
        for i in range(len(arr)-2, -1, -1):
            if(arr[i][j].isdigit()):
                num+=int(arr[i][j])*(10**len(str(num)))
        if(num!=0):
            add*=int(num/10)

print(out+add)
