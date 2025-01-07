# write a simple assymetric encryption program raw wuthout any library
# using RSA algorithm
# and save the keys in a file 

import random
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, math.isqrt(n)+1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair():
    p = random.randint(100, 1000)
    while not is_prime(p):
        p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    while not is_prime(q):
        q = random.randint(100, 1000)
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randint(2, phi-1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi-1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

public_key, private_key = generate_keypair()
print(f'Public key: {public_key}')
print(f'Private key: {private_key}')

message = 'Hello, World!'
print(f'Message: {message}')


