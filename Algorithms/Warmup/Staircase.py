__author__ = 'Tobias'

staircase_size = int(raw_input())

for i in xrange(staircase_size):
    i = (i + 1)
    print " " * (staircase_size - i) + "#" * i