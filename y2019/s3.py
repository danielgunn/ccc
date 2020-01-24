from random import randint

maxN = 10000000


def fill_in_dependencies(state):
    has = True  # assume there are some dependencies
    while (has):  # as long as we keep filling in dependencies we can keep going
        has = False
        for r in range(3):
            for c in range(3):
                if state[r][c] is None:
                    # look at this row
                    if (c == 0):
                        if (state[r][1] != None) and (state[r][2] != None):
                            state[r][c] = 2 * state[r][1] - state[r][2]
                            has = True
                    elif (c == 1):
                        if (state[r][0] != None) and (state[r][2] != None):
                            state[r][c] = (state[r][0] + state[r][2]) // 2
                            if (2*state[r][c] != (state[r][0] + state[r][2])):
                                return None  # Integers only
                            has = True
                    else:
                        if (state[r][0] != None) and (state[r][1] != None):
                            state[r][c] = 2 * state[r][1] - state[r][0]
                            has = True

                    # look at this column
                    if (r == 0):
                        if (state[1][c] != None) and (state[2][c] != None):
                            state[r][c] = 2 * state[1][c] - state[2][c]
                            has = True
                    elif (r == 1):
                        if (state[0][c] != None) and (state[2][c] != None):
                            state[r][c] = (state[0][c] + state[2][c]) // 2
                            if (2*state[r][c] != (state[0][c] + state[2][c])):
                                return None  # Integers only
                            has = True
                    else:
                        if (state[0][c] != None) and (state[1][c] != None):
                            state[r][c] = 2 * state[1][c] - state[0][c]
                            has = True

                # corrupt value check
                if (state[r][c] is not None):
                    if ((state[r][c] > maxN) or (state[r][c] < -maxN)):
                        return None
    return state


def is_complete(state):
    complete = True
    for r in state:
        if None in r:
            complete = False
    return complete


def is_corrupt(state):
    for r in range(3):
        if 2 * (state[r][1]) - state[r][0] != state[r][2]:
            return True
    for c in range(3):
        if 2 * (state[1][c]) - state[0][c] != state[2][c]:
            return True
    return False


def guess_solutions(current_state):
    current_state = fill_in_dependencies(current_state)
    if current_state is None:
        return None

    if is_complete(current_state):
        if is_corrupt(current_state):
            return None
        return current_state

    # find the first unfilled position
    for r in range(3):
        for c in range(3):
            if current_state[r][c] is None:

                # lets try some other numbers we've already used
                guess = [x[:] for x in current_state]  # deep copy again
                check = None
                for r2 in current_state:
                    for g in r2:
                        if g is not None:
                            guess = [x[:] for x in current_state]
                            guess[r][c] = g
                            check = guess_solutions(guess)
                            if check is not None:
                                return check

                # ok, we still havent found a good solution :( try to try random numbers!
                while check is None:
                    guess = [x[:] for x in current_state]
                    guess[r][c] = int(randint(-maxN, maxN))
                    check = guess_solutions(guess)
                return check


def main():
    state = []
    for i in range(3):
        rs = input().split()
        r = []
        for j in range(3):
            if rs[j] == "X":
                r.append(None)
            else:
                r.append(int(rs[j]))
        state.append(r)

    state = guess_solutions(state)

    for r in range(3):
        print(state[r])
    # guess


if __name__ == "__main__":
    main()
