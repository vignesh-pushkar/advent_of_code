arr=[]
while(True):
    st = input()
    if(not st):
        break
    arr.append(st)
print(arr)
add=0
def f(s, l):
    if(l==0):
        return ""
    m = s.index(max(s))
    if(len(s[m:])<l):
        st = f(s[0:m], l-len(s[m:])) + s[m:]
    elif(len(s[m:])>l):
        st = s[m] + f(s[m+1:], l-1)
    else:
        st = s[m:]
    return st
n=12
for i in arr:
    st=f(i, n)
    su=0
    for j in range(0, len(st)):
        su+=int(st[j])*(10**(n-j-1))
    add+=su
print(add)
