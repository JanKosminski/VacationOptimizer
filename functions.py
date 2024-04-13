import pandas as pd


def calculate_easter(year: int):
    #  Jean Meeus astronomic algorythm
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    ll = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * ll) // 451
    month = (h + ll - 7 * m + 114) // 31
    day = ((h + ll - 7 * m + 114) % 31) + 1
    easter_str = f'{day}/{month}/{year}'
    easter_monday = pd.to_datetime(easter_str, dayfirst=True) + pd.DateOffset(days=1)
    corpus_christi = pd.to_datetime(easter_str, dayfirst=True) + pd.DateOffset(days=60)
    return easter_monday, corpus_christi


def longest_sequence_indexes(lst: list[int]):
    max_count = 0
    current_count = 0
    start_index = None

    for i, char in enumerate(lst):
        if char == 0:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                start_index = i - max_count + 1
        else:
            current_count = 0
    return list(range(start_index, start_index + max_count))


# splits list of ints based on their values groups consecutive series into sub-lists
def consec_val_list_split(list_of_indexes: list[int]) -> list[list]:
    output_list = []
    templst = []
    try:
        for i, char in enumerate(list_of_indexes):
            if (list_of_indexes[i]+1) == list_of_indexes[i+1]:
                templst.append(char)
            else:
                templst.append(char)
                output_list.append(templst.copy())
                templst.clear()
    except IndexError:
        templst.append(list_of_indexes[-1])
        output_list.append(templst.copy())
        templst.clear()
        return output_list


def indexes_of_val(lst: list[int]) -> list[int]:
    list_of_indexes = []
    for i, char in enumerate(lst):
        if char == 0:
            list_of_indexes.append(i)
    return list_of_indexes


# checks distance of indexes for selected sublist of whole list

def check_dist(consecutive_sublist: list, whole_list: list) -> list[int]:
    dist2prev = None
    result = []
    first_ind = whole_list.index(consecutive_sublist[0])
    try:
        if len(consecutive_sublist) > 1:
            last_ind = whole_list.index(consecutive_sublist[-1])
            # calculate distance to next and previous one in whole list
            dist2prev = abs(whole_list[abs(first_ind-1) % len(whole_list)] - consecutive_sublist[0]) - 1
            dist2next = abs(consecutive_sublist[-1] - whole_list[last_ind + 1]) - 1
        else:
            # dumb but it will crash without that assignment
            last_ind = first_ind
            dist2prev = abs(whole_list[first_ind - 1] - consecutive_sublist[0]) - 1
            dist2next = abs(consecutive_sublist[0] - whole_list[first_ind + 1]) - 1
    # catches error when there is no next thing on list
    except IndexError:
        # returns index of nearest previous free day and distance
        result = [dist2prev, whole_list[first_ind]]
    else:
        # returns index of previous free day and distance then distance to next and index of next free day
        result = [dist2prev, whole_list[first_ind], dist2next, whole_list[last_ind]]
    finally:
        print(result)
        return result


def is_in_sublist(char: int, checked_list: list[list[int]]) -> list:
    for i, sublist in enumerate(checked_list):
        if char in sublist:
            return sublist


def check_total_day_count(entry_data: list[int], consecutive_sublist, whole_list):
    dist2prev = entry_data[0]
    sublist1 = entry_data[1]
    sum_w_prev = len(consecutive_sublist) + len(is_in_sublist(sublist1, whole_list)) + dist2prev
    if dist2prev != 0:
        efficiency1 = dist2prev / sum_w_prev
    else:
        efficiency1 = None
    if len(entry_data) == 4:
        dist2next = entry_data[2]
        sublist2 = entry_data[3]
        sum_w_next = len(consecutive_sublist) + len(is_in_sublist(sublist2, whole_list)) + dist2next
        if dist2next != 0:
            efficiency2 = dist2next / sum_w_next
        else:
            efficiency2 = None
        print(f"Sum with previous: {sum_w_prev}, % used workdays {efficiency1}, sum with next: {sum_w_next}, % used workdays {efficiency2}")
    else:
        print(f"Sum with previous: {sum_w_prev}")


lsit = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]

whole_index_list = indexes_of_val(lsit)
print(whole_index_list)

org_indexes = consec_val_list_split(whole_index_list)
org_indexes.sort(key=len, reverse=True)

print(org_indexes)
for sub in org_indexes:
    distances = check_dist(sub, whole_index_list)
    amount = check_total_day_count(distances, sub, org_indexes)
