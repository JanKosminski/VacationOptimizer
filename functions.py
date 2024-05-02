import pandas as pd
from vac import *


def calculate_easter(year: int):
    #  Jean Meeus's astronomic algorythm from wikipedia how did he come up with this is beyond me
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


def assign(a, ub, lb, level, flag, tv, tw):
    # Helper function to assign values to a Node object
    a.ub = ub
    a.lb = lb
    a.level = level
    a.flag = flag
    a.tv = tv
    a.tw = tw


def upper_bound(tv, tw, idx, arr, capacity):
    # Calculate the upper bound of the current node
    value, weight = tv, tw
    for i in range(idx, len(arr)):
        if weight + arr[i].dist2next <= capacity:
            weight += arr[i].dist2next
            value -= arr[i].value
        else:
            value -= ((capacity - weight) / arr[i].dist2next) * arr[i].value
            break
    return value


def lower_bound(tv, tw, idx, arr, capacity):
    # Calculate the lower bound of the current node
    value, weight = tv, tw
    for i in range(idx, len(arr)):
        if weight + arr[i].dist2next <= capacity:
            weight += arr[i].dist2next
            value -= arr[i].value
        else:
            break
    return value


def solve(arr, capacity):
    arr.sort(key=lambda x: x.value / x.dist2next, reverse=True)

    current = Node()
    current.tv = current.tw = current.ub = current.lb = 0
    current.level = 0
    current.flag = False

    min_lb = 0
    final_lb = float('inf')

    curr_path = [False] * len(arr)
    final_path = [False] * len(arr)

    pq = list()
    pq.append(current)

    while pq:
        current = pq.pop(0)

        if current.ub > min_lb or current.ub >= final_lb:
            continue

        if current.level != 0:
            curr_path[current.level - 1] = current.flag

        if current.level == len(arr):
            if current.lb < final_lb:
                for i in range(len(arr)):
                    final_path[arr[i].idx] = curr_path[i]
                final_lb = current.lb
            continue

        level = current.level

        right = Node()
        right.ub = upper_bound(current.tv, current.tw, level + 1, arr, capacity)
        right.lb = lower_bound(current.tv, current.tw, level + 1, arr, capacity)
        assign(right, right.ub, right.lb, level + 1, False, current.tv, current.tw)

        left = Node()
        if current.tw + arr[current.level].dist2next <= capacity and not arr[current.level].selected:
            left.ub = upper_bound(
                current.tv - arr[level].value,
                current.tw + arr[level].dist2next,
                level + 1,
                arr,
                capacity
            )
            left.lb = lower_bound(
                current.tv - arr[level].value,
                current.tw + arr[level].dist2next,
                level + 1,
                arr,
                capacity
            )
            assign(
                left,
                left.ub,
                left.lb,
                level + 1,
                True,
                current.tv - arr[level].value,
                current.tw + arr[level].dist2next
            )

            # Mark the object as selected
            arr[current.level].selected = True

        else:
            left.ub = 1
            left.lb = 1

        min_lb = min(min_lb, left.lb)

        if min_lb >= left.ub:
            pq.append(left)
        if min_lb >= right.ub:
            pq.append(right)
    max_profit = -final_lb
    selected_objects = []
    for i in range(len(arr)):
        if final_path[i]:
            selected_objects.append(arr[i])
    return selected_objects


def create_date_table(start='2000-01-01', end='2050-12-31'):
    start_ts = pd.to_datetime(start).date()
    end_ts = pd.to_datetime(end).date()
    # record timestamp is empty for now
    dates = pd.DataFrame(columns=['Workday'],
                         index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'
    days_names = {
        i: name
        for i, name in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    }
    dates['Day'] = dates.index.dayofweek.map(days_names.get)
    dates['Month'] = dates.index.month
    dates.reset_index(inplace=True)
    dates.index.name = 'date_id'
    return dates
