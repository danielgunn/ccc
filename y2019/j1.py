def inputTeam():
    t = 3*int(input())
    t += 2*int(input())
    t += int(input())
    return t

def main():
    a = inputTeam()
    b = inputTeam()
    if a > b:
        print("A")
    elif b > a:
        print("B")
    else:
        print("T")

if __name__ == '__main__':
    main()