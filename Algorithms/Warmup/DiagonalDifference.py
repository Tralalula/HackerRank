matrixSize = int(raw_input())

leftDiagonalSum = 0
rightDiagonalSum = 0
for i in xrange(matrixSize):
    row = raw_input().split()
    leftDiagonalSum += int(row[i])
    rightDiagonalSum += int(row[-(i+1)])
    
print abs(leftDiagonalSum - rightDiagonalSum)