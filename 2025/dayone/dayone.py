n=''
pos=50
ct=0
while(True):
    n=input()
    if not n:
        break
    
    if(n[0]=='R'):
        pos+=int(n[1:])
        if(pos>99):
            pos = pos%100
    
    else:
        pos-=int(n[1:])
        if(pos<0):
            pos%=100
    
    if(pos==0):
        ct+=1
print(pos, ct)


