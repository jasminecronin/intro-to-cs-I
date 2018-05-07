# Prints the continuous summation of the integers from 1 to n
def print_triangular_numbers(n) :
    t = 0
    for i in range(n) :
        t = t + i + 1
        print( i + 1, "\t", t )

# Counts the number of digits in a given integer
def num_digits(n) :
    count = 0
    if n == 0 :
        count = 1
        return count
    elif n < 0 :
        n = abs(n)
    while n != 0:
        count = count + 1
        n = n // 10
    return count
    
