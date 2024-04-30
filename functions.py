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


def is_in_sublist(char: int, checked_list: list[list[int]]) -> list:
    # returns first sublist the variable is in
    for i, sublist in enumerate(checked_list):
        if char in sublist:
            return sublist
