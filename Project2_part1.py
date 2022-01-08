# Fibonacci series
n = int(input("Enter number of terms: "))
sum = 0
carry1 = 0
carry2 = 1
for i in range(n):
    print(sum)
    carry1 = carry2
    carry2 = sum
    sum = carry2 + carry1
    
