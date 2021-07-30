n = int(input())
nsum = int((n*(n+1))/2)
print(nsum)
n = int(input())
sum=0
for i in range(n+1):
    sum = sum+i
print(sum)
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
n = int(input())
print(sum(n))