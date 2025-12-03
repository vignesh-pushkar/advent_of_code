st = input()
sarr = st.split(",")
arr=[]
for i in sarr:
    j = i.split("-")
    arr.append(j)
out = 0
sig = 0
for i in arr:
    for j in range (int(i[0]), int(i[1])+1):
        stj = str(j)
        sig = 0
        stwo=0
        for k in range(1, len(stj)//2+1):
            if(len(stj)%k!=0):
                continue
            comp = stj[0:k]
            
            if(comp*(len(stj)//k)==stj):
                stwo = 1
                break
        if(stwo == 1):    
            out+=j
print(out)
