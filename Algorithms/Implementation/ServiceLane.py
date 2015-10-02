N, T = raw_input().split()

segments = [int(i) for i in raw_input().split()]
for _ in xrange(int(T)):
    i, j = raw_input().split()
    print min(segments[int(i): int(j) + 1])