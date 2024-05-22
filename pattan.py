#pattan

def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

# Example usage
number_pattern(5)





def down_right_angled_triangle_pattern(n):
    for i in range(n):
        print(' ' * i + '*' * (n - i))

# Example usage
down_right_angled_triangle_pattern(5)


def pyramid_pattern(n):
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))

# Example usage
pyramid_pattern(5)








def zero_one_pattern(rows):
    for i in range(rows):
        # Generate the pattern based on the index i
        pattern = ""
        for j in range(i+1):
            if (i+j) % 2 == 0:
                pattern += "0"
            else:
                pattern += "1"
        print(pattern)

# Example usage
zero_one_pattern(5)