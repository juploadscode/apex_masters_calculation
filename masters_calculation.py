def calculate_ap_needed_per_day(points_needed, days_left_in_split):
    ap_per_day = points_needed/days_left_in_split
    return round(ap_per_day, 1)


def calculate_ap_for_all_days_remaining(points, days):
    ap_set = dict()
    while days > 0:
        ap_per_day = points/days
        ap_set["Day " + str(days)] = round(ap_per_day, 1)
        days -= 1
    return ap_set


if __name__ == '__main__':
    GOAL_AP = 8000

    # I am currently at 6280
    current_ap = int(input('Enter your current arenas points:'))

    ap_needed = GOAL_AP - current_ap

    # The split actually ends in 29 days, but I want to aim for masters 1 week before the real end date.
    days_remaining = 22

    ap_needed_per_day = calculate_ap_needed_per_day(ap_needed, days_remaining)
    print("You need", ap_needed_per_day, "AP per day to hit masters before the split ends")

    ap_needed_for_all_remaining_days = calculate_ap_for_all_days_remaining(ap_needed, days_remaining)
    print("AP you would need per day for all remaining days assuming you do not play (Current AP stays the same):")
    print(ap_needed_for_all_remaining_days)
