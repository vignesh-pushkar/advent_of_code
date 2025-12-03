n=''
pos=50
ct=0
while(True):
    n=input()
    if not n:
        break
    
    if(n[0]=='R'):
        for i in range(0, int(n[1:])):
            pos+=1
            if(pos==100):
                pos = 0
            if(pos == 0):
                ct+=1
    
    else:
        for i in range(0, int(n[1:])):
            pos-=1
            if(pos==-1):
                pos = 99
            if(pos == 0):
                ct+=1
print(pos, ct)
    

