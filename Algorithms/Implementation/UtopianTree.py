def utopianTree(n):
    sum = 0
    for i in xrange(n + 1):
        if i % 2 == 0: sum += 1
        else: sum *= 2

    return sum

for i in xrange(int(raw_input())):
    print utopianTree(int(raw_input()))