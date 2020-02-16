import time

def main():
    n, k = map(int, input().split())
    #print(n,k)

    #stime = time.time()

    a = []
    for i in range(n):
        # 0 - this level
        # 1 - previous level
        r = [[int(x),int(x)] for x in input().split()]
        a.append(r)

    this = 0
    for level in range(2,k+1):
        this = (this + 1) % 2
        prev = (this + 1) % 2
        for r in range(n-level,-1,-1):
            for c in range(len(a[r])):
                a[r][c][this] = max(a[r+1][c][prev], a[r+1][c+1][prev], a[r][c][this])

    sum = 0
    for r in range(0,n-k+1):
        for c in a[r]:
            sum += c[this]
    print(sum)

    #etime = time.time()
    #print("time:", (etime - stime))
    # time: 57.030564069747925

if __name__ == "__main__":
    main()