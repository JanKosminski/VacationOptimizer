import datetime as dt
import calendar
import functions as fc
from vac import *


MONTHS = [calendar.month_name[i] for i in range(1, 13)]
# Capacity aka amount of paid leave days to use
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
    fc.print_out_solutions(solutions, org_indexes, calendar)

