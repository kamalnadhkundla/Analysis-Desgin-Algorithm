"""
Input: {"You", "are", "beautiful", "looking"}
Output: You are looking beautiful
"""

s = input().split()
n= len(s)
a = []
for st in s:
    a.append(len(st))
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            s[i],s[j]=s[j],s[i]
res = " ".join(s)
print(res)