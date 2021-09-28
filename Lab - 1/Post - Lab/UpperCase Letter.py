
"""
Input arr[] = poiNtEr aRRAy cOde foR
Output: [('cOde', 1), ('foR', 1), ('poiNtEr', 2), ('aRRAy', 3)]
"""
a=list(input().split(' '))
b=[]
c=[]
for i in range(len(a)):
    k=0
    b.append(a[i])
    s=a[i]
    for j in range(len(s)):
        if(s[j]>='A' and s[j]<='Z'):
            k+=1
    c.append(k)
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]>c[j]):
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
            t=c[i]
            c[i]=c[j]
            c[j]=t
for i in range(len(b)):
    print([b[i],c[i]],end=",")
