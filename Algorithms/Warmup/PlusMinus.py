def plusMinus(numerator, denominator):
    return "%.3f" % float(numerator / denominator)

lstSize = int(raw_input())
lst = raw_input().split()

numOfPositive = 0.0
numOfNegative = 0.0
numOfZero     = 0.0

for i in lst:
    number = int(i)
    if   number > 0: numOfPositive += 1
    elif number < 0: numOfNegative += 1
    else           : numOfZero     += 1

print plusMinus(numOfPositive, lstSize)
print plusMinus(numOfNegative, lstSize)
print plusMinus(numOfZero,     lstSize)