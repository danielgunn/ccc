def main():
    s = input()
    print(s)
    s = s.split()
    n = int(s[0])
    k = int(s[1])
    print(n,k)
    a = []
    for i in range(n):
        r = input()
        r = r.split()
        r = list(map(int, r))
        a.append(r)

    sum = 0
    # for each root
    for r in range(n-k+1):
        for c in range(r+1):
            # for each sub-tree of size k

            m =  a[r][c]
            cl = 2
            for r2 in range(r+1,r+k):
                for c2 in range(c,c+cl):
                    v = a[r2][c2]
                    m = max(m, a[r2][c2])
                cl += 1
            sum += m

    print(sum)

if __name__ == "__main__":
    main()