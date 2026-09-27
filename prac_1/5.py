N = int(input("Введите N: "))

is_prime = []
for i in range(N + 1):
    is_prime.append(True)

if N >= 0:
    is_prime[0] = False
if N >= 1:
    is_prime[1] = False

for p in range(2, N + 1):
    if is_prime[p] == True:
        # p — простое, вычёркиваем все его кратные, начиная с p*p
        for multiple in range(p * p, N + 1, p):
            is_prime[multiple] = False

print("Простые числа от 2 до", N, ":")
for i in range(2, N + 1):
    if is_prime[i] == True:
        print(i, end=" ")
print()