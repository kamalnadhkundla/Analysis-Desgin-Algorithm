"""
Suppose a merge sort algorithm, for input size 64, takes 30 secs in the worst case.
What is the maximum input size that can be calculated in 6 minutes (approximately)?

Time complexity of merge sort is Θ(nLogn)

c*64Log64 is 30
c*64*6 is 30
c is 5/64

For time 6 minutes

5/64*nLogn = 6*60

nLogn = 72*64 = 512 * 9

n = 512.
"""