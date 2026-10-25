N = int(input("Enter a number: "))
primes = 0
print("Prime numbers: ", end='')
i = 2
while primes < N:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')
        primes += 1
    i += 1