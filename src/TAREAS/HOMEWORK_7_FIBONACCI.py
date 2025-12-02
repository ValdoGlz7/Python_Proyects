"""
    FIBONACCI SERIES

    What is the fibonacci series?
    The fibonacci series is the series where each number that
    is part of it is the sum of the past 2 numbers, usualy starting
    in the number 0 or 1.
    
    What does "cacluculate the seires of 'n' number" mean?
    It means to generate the fibonaci up to the 'n' number.
    
    What will your program do?
    It will generate the fibonacci series until the 'n' number
    of the series is reached.
"""
#Number of elements:
n = int(input("How many elements do you want? "))

a, b = 0, 1
for i in range(n):
    a, b = b, a + b
    print(a)