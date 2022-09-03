def fib(n):
    if n < 1 or type(n) != int:
        print('You need to input a positive integer.')
        quit()
    elif n in (1, 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)
          
print(fib(10))



