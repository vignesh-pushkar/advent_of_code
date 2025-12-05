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
a = [ [int(x[0]), int(x[1])] for x in a]
a.sort()
print(a)
ct=0

pt=0
for i in a:
    if(i[0]>pt):
        ct+=i[1]-i[0]+1
    elif(i[1]>pt):
        ct+=i[1]-pt
    if(i[1]>pt):
        pt=i[1]
    print(i[0], i[1], ct, pt)    
    
#brute force
'''
af=min([int(x[0]) for x in a])
al=max([int(x[1]) for x in a])
print(af, al)
for i in range(af, al+1):
    for j in a:
        if(int(j[0])<=i and i<=int(j[1])):
            ct+=1
            break
    '''
print(ct)
