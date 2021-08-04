"""
Input
5
Neil 	Katherine 	Harry 		Stefan 		Dennis
Output
Dennis	Harry 		Katherine 	Neil 		Stefan
"""

p=['Neil','Katheriene','Herry','Stefan','Dennis']
b=[]
c=[]
for i in range(0,len(p)):
  if(i%2==0):
    b.append(p[i])
  else:
    c.append(p[i])
b.sort()
c.sort()
print(sorted(b+c))
