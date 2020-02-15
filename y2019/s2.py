from numba import njit
import numpy as np

maxN = 1000000

# Using an optimized version of Sieve of Eratosthenes
# Credits:  Giuseppe Vettigli 
# https://dzone.com/articles/speeding-up-the-sieve-of-eratosthenes-with-numba
@njit
def sieve_python_jit(limit):
    is_prime = np.full(limit, True)
    is_prime[0] = False
    is_prime[1] = False
    for d in range(2, int(np.sqrt(limit) + 1)):
        if is_prime[d]:
            for n in range(d*d, limit, d):
                is_prime[n] = False
    return is_prime


def main():
    t = int(input())

    prime = sieve_python_jit(maxN * 2)

    for i in range(t):
        n = int(input())

        for a in range(2, maxN * 2):
            if prime[a]:
                b = 2*n - a
                if prime[b]:
                    print("{0} {1}".format(a,b))
                    break

if __name__ == '__main__':
    main()