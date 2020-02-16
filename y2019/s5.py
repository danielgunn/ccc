import numpy as np
from numba import njit

@njit
def find_total(n,k,a):
    flip = True
    for level in range(2, k + 1):
        flip = not flip
        for r in range(n - level, -1, -1):
            for c in range(r + 1):
                if flip:
                    a[r, c] = max(a[c, r + 2], a[c + 1, r + 2], a[r, c])
                else:
                    a[c, r + 1] = max(a[r + 1, c], a[r + 1, c + 1], a[r, c])

    tot = 0
    if flip:
        for r in range(0, n - k + 1):
            for c in range(r + 1):
                tot += a[r, c]
    else:
        for r in range(n):
            for c in range(r + 1, n - k + 2):
                tot += a[r, c]
    return tot

def main():
    n, k = map(int, input().split())
    #print(n,k)

    #stime = time.time()

    # We will store the triangle in a matrix
    # (r,c) - store the value of the maximum triangle at this level
    # (c,r+1) - store the previous level's maximum triangle
    a = np.empty((n,n+1), int)
    for r in range(n):
        # 0 - this level
        # 1 - previous level
        x = input().split()
        for c in range(len(x)):
            a[r,c] = x[c]
            a[c,r+1] = x[c]

    tot = find_total(n,k,a)
    print(tot)

    #etime = time.time()
    #print("time:", (etime - stime))
    #time: 0.5824160575866699

if __name__ == "__main__":
    main()