from math import sqrt

def getPerfectSquares(m, n):
    mSqrt = int(sqrt(m))
    nSqrt = int(sqrt(n))

    count = 0
    for i in xrange(mSqrt, (nSqrt + 1)):
        value = i ** 2
        if value >= m and value <= n: count += 1

    return count

for _ in xrange(int(raw_input())):
    mn = raw_input().split()
    print getPerfectSquares(int(mn[0]), int(mn[1]))