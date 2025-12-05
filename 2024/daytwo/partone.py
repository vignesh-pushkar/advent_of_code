data=[]
while(True):
    st = input()cd
    if(not st):
        break
    data.append(st.split())
ct=0
gd=0

def check(arr):
    
for i in data:
    i =[int(x) for x in i]
    sig=0
    gd=0
    for j in range(1, len(i)):
        if(not (0<i[j]-i[j-1] and i[j]-i[j-1]<=3)):
            gd+=1
            if(not (0<i[j]-i[j-2] and i[j]-i[j-2]<=3)):
                if(j+1==len(i)):
                    pass
                elif(not (0<i[j+1]-i[j-1] and i[j+1]-i[j-1]<=3)):
                    gd+=1
                else:
                    i[j]=i[j-1]
        if(gd>1):
            sig+=1
            break
    gd=0
    i =[int(x) for x in i]
    for j in range(1, len(i)):
        if(not (-3<=i[j]-i[j-1] and i[j]-i[j-1]<0)):
            gd+=1
            if(not (-3<i[j]-i[j-2] and i[j]-i[j-2]<=0)):
                if(j+1==len(i)):
                    pass
                elif(not (-3<i[j+1]-i[j-1] and i[j+1]-i[j-1]<=0)):
                    gd+=1
                else:
                    i[j]=i[j-1]
        if(gd>1):
            sig+=1
            break
    if(sig==2):
        ct+=1  
print(1000-ct)
