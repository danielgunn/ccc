goal_state = None
rules = []

# returns the sequence of steps needed to find the goal
# it might return 0: meaning it cannot find a solution
# it might return "": meaning no steps are needed, its already solved
def find_solution_steps(state, steps_remaining):
    if steps_remaining < 1:
        if state == goal_state:
            return ""  # already solved
        else:
            return 0  # no solution found

    # lets try all the rules
    for nule_num in range(len(rules)):
        attempt = rules[nule_num]

        # lets try this rule on all possible positions
        for pos in range(len(state) - attempt[2] + 1):
            count = 0
            if state[pos:pos + attempt[2]] == attempt[0]:
                # potential rule
                s2 = state[:pos] + attempt[1] + state[pos + attempt[2]:]

                seq = find_solution_steps(s2, steps_remaining - 1)  # recursion!
                if seq != 0: # Wow we found a solution!
                    return "{0} {1} {2}\n{3}".format(nule_num + 1, pos + 1, s2, seq)
    return 0

def main():
    global goal_state
    global rules

    rules = []

    # for convenience: a rule will be defined as:
    # 0 - a start state string
    # 1 - a end state string
    # 2 - the length of the start state
    # 3 - the length of the end state
    for i in range(3):
        l = input().split()
        l.append(len(l[0]))
        l.append(len(l[1]))
        rules.append(l)

    l = input().split()
    goal_state = l[2]

    seq = find_solution_steps(l[1], int(l[0]))
    print(seq)


if __name__ == "__main__":
    main()