import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
decoded_string = ""
for j in range(m):
    for i in range(n):
        decoded_string += matrix[i][j]
pattern = r"(?<=\w)([^\w]+)(?=\w)"
final_output = re.sub(pattern, " ", decoded_string)
print(final_output)
