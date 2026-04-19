n = 1079
e = 43
c = [996, 894, 379, 631, 894, 82, 379, 852, 631, 677, 677, 194, 893]

# n is consisted of two prime numbers (p, q) -> find factors of n
p = 13
q = 83

# Euler's Totient Function (phi_n)
phi_n = (p-1)*(q-1)

# Need to find d -> e*d = 1 mod phi_n (where e*d % phi_n = 1)
for k in range(1, 10001):
    d = (1 + (k * phi_n)) / e
    if d.is_integer():
        break
d = int(d)

# Use M = (C^d) % n to decipher
m = ""
for char in c:
    m += chr((char ** d) % n)
print(m)