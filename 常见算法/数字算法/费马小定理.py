"""
Q is N prime
is_prime N
pick random a<N
if a**(N-1)mod N==1 return True
else reurn False
"""
import random

def is_prime(N):
    if random.randrange(N)**(N-1)%N==1:
        return True
    else:
        return False

def is_prime_super(N, k):
    for _ in range(k):
        if random.randrange(N)**(N-1)%N!=1:
            return False
    return True

def random_prime(N):
    while True:
        a=random.randrange(N)
        if is_prime_super(a, 100):
            return a
print(random_prime(10086))