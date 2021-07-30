"""
Input
a1b2c3d4e

Output
abbdcfdhe
Explanation:
The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
"""

s = input()
lst = list(s)
for i in range(1,len(lst),2):
    lst[i] = chr(ord(lst[i-1]) + int(lst[i]))
s = "".join(lst)
print(s)