"""
Input: arr[] = {1, 2, 3, 4, 5, 6}
{1, 1, 2, 1, 2, 2}
Output: 3 5 6 1 2 4
"""

def numofsetbits(n):
    st=''
    while(n>0):
        st+=str(n&1)
        n=n>>1
    return st.count('1')

lst=list(map(int,input().split()))
res=[]
for i in lst:
    res.append(numofsetbits(i))
for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if(res[j]<res[j+1]):
            res[j],res[j+1]=res[j+1],res[j]
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
