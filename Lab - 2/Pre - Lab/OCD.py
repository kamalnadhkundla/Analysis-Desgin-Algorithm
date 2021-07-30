"""
Input:
aaabbc
cbbaaa

Output
aabbcc
aabbcc
"""

def countFrequency(string, ch):
  count = 0
  for i in range(len(string)):
    if(string[i] == ch):
      count = count+1
  return count

def sortArr(string):
  n = len(string)

  vp = []

  for i in range(n):
    vp.append((countFrequency(string, string[i]), string[i]));

  vp.sort();
  for x in range(len(vp)):
    print(vp[x][1],end="")

string = input()
sortArr(string); 