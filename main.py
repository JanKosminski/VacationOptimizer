import datetime as dt
import calendar
from gui_module import *

MONTHS = [calendar.month_name[i] for i in range(1, 13)]
CAPACITY = 20


if __name__ == "__main__":
    # grab date
    today = dt.datetime.now()
    year = today.year
    # set calendar df
    calendar = create_date_table(start=f"{today.year}-{today.month}-{today.day}", end=f"{today.year}-12-31")
    holiday_setup(calendar, year)
    # get workdays to list
    lsit = calendar['Workday'].to_list()
    # prepare and organize the workdays list
    whole_index_list = indexes_of_val(lsit)
    org_indexes = consec_val_list_split(whole_index_list)
    # generate Vac objects array
    object_list = []
    for i, it in enumerate(org_indexes):
        object_list.append(Vacation(nums=it, whole_list=whole_index_list, idx=i))
    # remove last object that has no next free day (most likely last one)
    for j in object_list:
        if j.next_ind is None:
            object_list.remove(j)
    # feed functions to gui module
    kwargs = {"arr": object_list, "calendar": calendar, "org_indexes": org_indexes}
    gui(solve, **kwargs)


