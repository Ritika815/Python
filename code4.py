def prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
c=0
t=int(input("Enter the no"))
for n in range(1,t):
    x = prime(n)
    c += x
print("Total prime numbers in range :", c)