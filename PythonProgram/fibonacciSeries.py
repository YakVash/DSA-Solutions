def fib_iterative(n) :
    
    """
    Print the first n Fibonacci numbers (starting with 0, 1).
    """
    if n <= 0 :

        print("No terms.")
        return
    
    if n == 1 :

        print(0)
        return
    
    a = 0
    b = 1

    # print first two
    print(a, end=" ")
    print(b, end=" ")

    # print remaining
    for _ in range(3, n + 1) :

        c = a + b
        print(c, end=" ")
        a = b
        b = c

    print() # newline at end

# Example usage:
fib_iterative(10)