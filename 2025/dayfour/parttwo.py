arr=[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st)
h=len(arr)
w=len(arr[0])
out = 1
var=0
while(out!=0):
    out=0
    two = arr.copy()
    for i in range(0, h):
        for j in range(0, w):
            ct=0
            if(arr[i][j]=='@'):
                #upper line check
                if(i>0 and arr[i-1][j]=='@'):
                    ct+=1
                if(i>0 and j>0 and arr[i-1][j-1]=='@'):
                    ct+=1
                if(i>0 and j<w-1 and arr[i-1][j+1]=='@'):
                    ct+=1
                    
                #lower line check
                if(i<h-1 and arr[i+1][j]=='@'):
                    ct+=1
                if(i<h-1 and j>0 and arr[i+1][j-1]=='@'):
                    ct+=1
                if(i<h-1 and j<w-1 and arr[i+1][j+1]=='@'):
                    ct+=1
                
                #inline check
                if(j>0 and arr[i][j-1] == '@'):
                    ct+=1
                if(j<w-1 and arr[i][j+1]=='@'):
                    ct+=1
                    
                if(ct<4):
                    out+=1
                    two[i]=two[i][:j] + 'x' + two[i][j+1:]
    arr = two.copy()
    var+=out
    print(var)


print(var)
