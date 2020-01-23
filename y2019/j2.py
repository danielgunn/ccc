def main():
    n = int(input())
    for i in range(n):
        l = input()
        a = l.split(" ")
        print(a[1]*int(a[0]))

if __name__ == '__main__':
    main()