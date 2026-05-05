import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    lines = []  
    for i in range(size):
        s = "-".join(alphabet[size-1:size-i-1:-1] + alphabet[size-i-1:size])
        lines.append(s.center(width, "-"))
    print('\n'.join(lines + lines[::-1][1:]))
