def findDigits(n):
    count = 0
    for i in n:
        if int(i) == 0:
            continue
        elif (float(n) / int(i)).is_integer():
            count += 1
    return count

for _ in xrange(int(raw_input())):
    print findDigits(raw_input())