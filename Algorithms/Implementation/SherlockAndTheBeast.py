def decent_number(i):
    j = 5 * ((2 * i) % 3)
    if j > i:
        return -1
    return '5' * (i - j) + '3' * j

num_of_test_cases = int(raw_input())
for i in xrange(num_of_test_cases):
    number_of_digits = int(raw_input())
    print decent_number(number_of_digits)