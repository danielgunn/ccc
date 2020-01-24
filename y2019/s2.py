maxN = 1000000

# Modified from https://www.geeksforgeeks.org/sieve-of-eratosthenes/
def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return prime


def main():
    t = int(input())

    prime = SieveOfEratosthenes(maxN * 2)

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