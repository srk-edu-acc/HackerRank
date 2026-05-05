import numpy
N = int(input())
matrix = numpy.array([input().split() for _ in range(N)], float)
det_value = numpy.linalg.det(matrix)
print(round(det_value, 2))
