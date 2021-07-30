"""
Input: arr[] = {1, 2, 3, 4, 5, 6}
{1, 1, 2, 1, 2, 2}
Output: 3 5 6 1 2 4
"""

arr = list(map(int,input().split()))
n= len(arr)
a = []
for x in arr:
    bin_x = bin(x)
    res = list(bin_x)
    res = res[2:]
    a.append(res.count('1'))

for i in range(n-1):
    for j in range(i+1,n):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
            arr[i],arr[j]=arr[j],arr[i]
print(arr)