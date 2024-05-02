import datetime as dt
import calendar
from functions import *
from vac import *
import itertools

MONTHS = [calendar.month_name[i] for i in range(1, 13)]
CAPACITY = 20


if __name__ == "__main__":
    # grab date
    today = dt.datetime.now()
    year = today.year

    # set calendar df
    calendar = create_date_table(start=f"{today.year}-{today.month}-{today.day}", end=f"{today.year}-12-31")

    # set free days on weekends
    for i in calendar.index:
        if calendar['Day'][i] == "Sunday" or calendar['Day'][i] == 'Saturday':
            calendar.at[i, 'Workday'] = 0
        else:
            calendar.at[i, 'Workday'] = 1

    # set work-free days on holidays
    holidays = [f"{year}-01-01", f"{year}-01-06", f"{year}-05-01", f"{year}-05-03", f"{year}-08-15",
                f"{year}-11-1", f"{year}-11-11", f"{year}-12-25", f"{year}-12-26"]
    easter, corpus = calculate_easter(year)
    holidays_dt = [pd.to_datetime(w, yearfirst=True) for w in holidays]
    holidays_dt.extend(calculate_easter(int(year)))

    for date in holidays_dt:
        if date in calendar['Date'].values:
            # grabbing index returns index datatype, getting its value returns a list, need to get first item of it.
            a = calendar.index[calendar['Date'] == date].values[0]
            calendar.at[a, 'Workday'] = 0

    # get workdays to list
    lsit = calendar['Workday'].to_list()
    # prepare and organize the workdays list
    whole_index_list = indexes_of_val(lsit)
    org_indexes = consec_val_list_split(whole_index_list)
    # generate Vac objects array
    object_list = []
    for i, it in enumerate(org_indexes):
        object_list.append(Vacation(nums=it, whole_list=whole_index_list, idx=i))
    # remove last object that has no next free day
    for j in object_list:
        if j.next_ind is None:
            object_list.remove(j)
    # solve branch bound LC method
    solutions = solve(object_list, CAPACITY)
    # input indexes of free days
    day_indexes = []
    for a in solutions:
        day_indexes.append(a.indexes)
        day_indexes.append([i for i in range(a.indexes[-1] + 1, a.next_ind)])
        day_indexes.append(is_in_sublist(a.next_ind, org_indexes))
    day_indexes = list(set(list(itertools.chain.from_iterable(day_indexes))))
    print(f"Total length of free days is {len(day_indexes)}")

    # test if it works

    organized_solutions = consec_val_list_split(day_indexes)
    print(organized_solutions)
    for o in organized_solutions:
        print(f"Vacations from {calendar.at[o[0], 'Date']} to {calendar.at[o[-1], 'Date']}")
        print(f"Total length {len(o)}")
