

# euclid's algorithm finds the greatest common divisor of two numbers
# by repeatedly dividing the larger of two with the smaller number, then setting
# the smaller number to be the larger, and the remainder to be the smaller number
# for the next iteration. the algorithm stops when the remainder is 0 in which
# the greatest common divisor of the initial two numbers is the last non-zero remainder
# note in this implementation we're considering only positive integers

def gcd(a, b):
    larger = max(a, b)
    smaller = min(a, b)

    while larger % smaller != 0:
        remainder = (larger % smaller)
        # uncomment the line below to see how the algorithm works line by line
        # print(str(larger), '=', 'quotient x', str(smaller), '+', str(remainder), '\n')
        larger = smaller
        smaller = remainder
    return smaller


# given two integers, a, b that a x b = gcd(a, b) x lcm(a, b) we can also
# define the function lcm(a, b) (lowest common multiple of a and b) using gcd(a, b)

def lcm(a, b):
    return int(a * b / gcd(a, b))
