for _ in xrange(int(raw_input())):
    N, C, M = [int(i) for i in raw_input().split()]
    x = N / C
    numWrappers = x

    while (x - M) >= 0:
        numWrappers += 1
        x -= (M - 1)

    print numWrappers