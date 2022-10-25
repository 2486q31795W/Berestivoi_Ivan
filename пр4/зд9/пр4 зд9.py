a = int(input())
fib1 = 0
fib2 = 1
b = 0
sum = 0
for c in range (0, a):
    sum = sum + fib1
    b = fib1 + fib2
    fib1 = fib2 
    fib2 = b
    print(sum)
