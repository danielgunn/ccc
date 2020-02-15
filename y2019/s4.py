a = []

def find_maximum_score(max_day_length, num_days_left, starting_activity_index, num_activities):
    global a
    if max_day_length * num_days_left < num_activities:
        return -1

    if num_activities < 0:
        return -1

    if num_days_left < 1:
        if (num_activities == 0):
            return 0
        return -1

    # how many activities should we do today?
    best_score = 0
    min_day_length = num_activities % max_day_length
    if min_day_length == 0:
        min_day_length = max_day_length

    assert(min_day_length <= num_activities)

    for today_length in range(min_day_length, max_day_length + 1):
        score = find_maximum_score(max_day_length, num_days_left - 1, starting_activity_index + today_length, num_activities-today_length)
        if score == -1:
            continue
        else:
            todays_score = 0
            for i in range(today_length):
                todays_score = max(todays_score, a[starting_activity_index + i])
            best_score = max(best_score, score + todays_score)
    return best_score

def main():
    global a
    # inputing and formatting the num_attractions, long_day_length and a variables
    t = input()
    t = t.split()
    num_attractions = int(t[0]) # total number of attractions
    max_day_length = int(t[1]) # number of attractions per day
    t = input()
    t = t.split()
    a = []
    for i in t:
        a.append(int(i))

    num_days = num_attractions//max_day_length # full num_full_days
    min_day_length = num_attractions%max_day_length # remainder (length of short day)
    if min_day_length !=0:
        num_days += 1

    ms = find_maximum_score(max_day_length, num_days, 0, num_attractions)
    print(ms)

if __name__ == "__main__":
    main()