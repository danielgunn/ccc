def main():
    n = int(input())
    for i in range(n):
        line = input()
        char_count = 0
        prev_char = line[0]
        for cur_char in line:
            if cur_char == prev_char:
                char_count+=1
            else:
                print("{0} {1} ".format(char_count, prev_char), end="")
                prev_char = cur_char
                char_count = 1
        print("{0} {1}".format(char_count, prev_char))

if __name__ == '__main__':
    main()