arr=[]
while(True):
    st=input()
    if(not st):
        break
    arr.append(st)

ct=0
def counter(st, d, ct):
    ind=st.copy()
    if(d<len(arr)-1):
        for j in st:
            if(arr[d+1][j]=='^'):
                ct+=1
                ind.add(j+1)
                ind.add(j-1)
        ct+=counter(ind, d+1, ct)
        return ct
    else:
        return ct

ars=arr.copy()
ind={arr[0].find('S')}
tmls=1
for i in range(1, len(arr)):
    s=ind.copy()
    d=-1
    for j in ind:
        if(arr[i][j]=='^'):
            s.add(j-1)
            s.add(j+1)
            ars[i]=ars[i][0:j-1]+'|'+'^'+'|'+ars[i][j+2:]
            s.remove(j)
            ct+=1
        else:
            ars[i]=ars[i][:j]+'|'+ars[i][j+1:]
    
    ind=s.copy()
for i in ars:
    print(i)
print("splits: ", ct)

paths=[[0 for i in range(len(arr[0]))] for j in range(len(arr))]

h=len(arr)-1
while(h>0):    
    for j in range(0, len(ars[0])):
        if(h==len(arr)-1 and ars[h][j]=='|'):
            paths[h][j]=1
            paths[h-1][j]=1
            
        elif(ars[h][j]=='^'):
            paths[h-1][j]=paths[h][j-1]+paths[h][j+1]
        
        elif(ars[h][j]=='|' and ars[h-1][j]=='|'):
            paths[h-1][j]=paths[h][j] 
    h-=1  

    
print("timelines: ", paths[1][arr[0].find("S")])        
    
    
                  
    
