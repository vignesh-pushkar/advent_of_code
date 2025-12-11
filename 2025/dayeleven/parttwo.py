arr=[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st.split())


for i in arr:
    i[0]=i[0][:3]

car=[]
for i in arr:
    car.append([i[0], -1])
dic={}
for i in arr:
    dic[i[0]]=i[1:]

def counter(ind, dac, fft):
    if 'out' in arr[ind][1:]:
        if(dac==1 and fft==1):    
            print("here")
            return 1
        return 0
    ct=0
    for i in arr[ind][1:]:
        for j in arr:
            if(i==j[0]):
                if(i=="dac"):
                    ct+= counter(arr.index(j), 1, fft)
                elif(i=="fft"):
                    ct+= counter(arr.index(j), dac, 1)
                else:
                    ct+= counter(arr.index(j), dac, fft)
    return ct

def counter2(st, dac, fft):
    if 'out' in dic[st]:     
        if(dac==1 and fft==1):    
            print("here")
            return 1
        return 0
    ct=0
    for i in dic[st]:
        #ct+=counter2(i, dac, fft)
        if(i=="dac"):
            ct+= counter2(i, 1, fft)
        elif(i=="fft"):
            ct+= counter2(i, dac, 1)
        else:
            ct+= counter2(i, dac, fft)
    return ct

'''
for i in arr:
    if(i[0]=="svr"):
        out=counter(arr.index(i), 0, 0)
        break
'''
out=counter2('svr', 0, 0)
print(out)
