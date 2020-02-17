import numpy as np
from numba import njit

@njit
def find_maximum_score(a, max_day_length, num_days_left, starting_activity_index, num_activities):
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

    # assert(min_day_length <= num_activities)

    for today_length in range(min_day_length, max_day_length + 1):
        score = find_maximum_score(a, max_day_length, num_days_left - 1, starting_activity_index + today_length, num_activities-today_length)
        if score == -1:
            continue

        todays_score = np.max(a[starting_activity_index:starting_activity_index+today_length])

        best_score = max(best_score, score + todays_score)
    return best_score

def main():
    # inputing and formatting the num_attractions, long_day_length and a variables
    num_attractions, max_day_length = map(int, input().split())

    a = np.fromstring(input(), dtype=int, sep=" ")

    num_days = num_attractions//max_day_length # full num_full_days
    min_day_length = num_attractions%max_day_length # remainder (length of short day)
    if min_day_length !=0:
        num_days += 1

    ms = find_maximum_score(a, max_day_length, num_days, 0, num_attractions)
    print(ms)

if __name__ == "__main__":
    main()