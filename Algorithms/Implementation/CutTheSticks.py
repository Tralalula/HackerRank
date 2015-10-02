N = int(raw_input())
sticks = [int(i) for i in raw_input().split()]

while True:
    numOfSticks = sum(i > 0 for i in sticks)
    if numOfSticks > 0:
        print numOfSticks

    if numOfSticks <= 1:
        break

    stickCut = min(i for i in sticks if i > 0)
    sticks = map(lambda x: x - stickCut, sticks)