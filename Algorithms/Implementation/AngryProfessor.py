num_of_test_casees = int(raw_input())

for i in xrange(num_of_test_casees):
    class_size_requirements = raw_input()
    class_size_requirements = class_size_requirements.split()
    student_arrival_times = raw_input()
    student_arrival_times = student_arrival_times.split()
    num_of_students = int(class_size_requirements[0])
    min_class_size = int(class_size_requirements[-1])

    num_of_students_on_time = 0
    for j in xrange(num_of_students):
        if int(student_arrival_times[j]) <= 0:
            num_of_students_on_time += 1

    if num_of_students_on_time >= min_class_size:
        print "NO"
    else:
        print "YES"