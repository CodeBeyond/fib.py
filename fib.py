def fib(num):
    """Takes a positive integer parameter and returns the number at that position of the Fibonacci sequence."""
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
