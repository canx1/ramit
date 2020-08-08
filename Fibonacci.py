## Number of fib numbers required
n = 20

# Set a and b to the first two numbers in the sequence
a = 0
b = 1 

# List in which to store numbers
fib_nums = []

# Use a for loop to create the sequence, repeat n times
for i in range(n):
    fib_nums.append(a)
    a,b = b,a+b     
    
print(f'The first {n} Fibonacci numbers are, {fib_nums}')
