def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i).split('o')[-1]
        hexadecimal = hex(i).split('x')[-1].upper()
        binary = bin(i).split('b')[-1]
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")
