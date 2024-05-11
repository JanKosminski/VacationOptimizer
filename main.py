import datetime as dt
import calendar
import functions as fc
from vac import *
import itertools

MONTHS = [calendar.month_name[i] for i in range(1, 13)]
CAPACITY = 20


def clean_object_list(org_list):
    object_list = []
    for i, it in enumerate(org_list):
        object_list.append(Vacation(nums=it, whole_list=whole_index_list, idx=i))
    # remove last object that has no next free day
    for j in object_list:
        if j.next_ind is None:
            object_list.remove(j)
    return object_list


if __name__ == "__main__":
    # grab date
    today = dt.datetime.now()
    year = today.year
    # set calendar df
    calendar = fc.create_date_table(start=f"{today.year}-{today.month}-{today.day}", end=f"{today.year}-12-31")
    fc.innit_holidays(calendar, year)
    # get workdays to list
    lsit = calendar['Workday'].to_list()
    # prepare and organize the workdays list
    whole_index_list = fc.indexes_of_val(lsit)
    org_indexes = fc.consec_val_list_split(whole_index_list)
    # generate Vac objects array
    object_list = clean_object_list(org_indexes)
    # solve branch bound LC method
    solutions = fc.solve(object_list, CAPACITY)
    # input indexes of free days
    day_indexes = []
    for a in solutions:
        day_indexes.append(a.indexes)
        day_indexes.append([i for i in range(a.indexes[-1] + 1, a.next_ind)])
        day_indexes.append(fc.is_in_sublist(a.next_ind, org_indexes))
    day_indexes = list(set(list(itertools.chain.from_iterable(day_indexes))))

    print(f"Total length of free days is {len(day_indexes)}")

    # test if it works
    day_indexes.sort(reverse=False)
    organized_solutions = fc.consec_val_list_split(day_indexes)
    print(organized_solutions)
    for o in organized_solutions:
        print(f"Vacations from {calendar.at[o[0], 'Date']} to {calendar.at[o[-1], 'Date']}")
        print(f"Total length {len(o)}")
