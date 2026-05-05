import numpy
N, M = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(N)], int)
min_axis_1 = numpy.min(my_array, axis=1)
print(numpy.max(min_axis_1))
