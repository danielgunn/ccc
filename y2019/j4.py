def main():
    l = input()
    nh = l.count("H") % 2
    nv = l.count("V") % 2
    score = nh *2 + nv
    answer = ["1 2\n3 4", "2 1\n4 3", "3 4\n1 2", "4 3\n2 1"]
    print(answer[score])

if __name__ == '__main__':
    main()