from functions import *
from vac import *
import copy
import itertools
from gui_module import *
CAPACITY = 8

lsit = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
whole_index_list = indexes_of_val(lsit)
print(whole_index_list)

org_indexes = consec_val_list_split(whole_index_list)
print(org_indexes)
object_list = []
for i, it in enumerate(org_indexes):
    object_list.append(Vacation(nums=it, whole_list=whole_index_list, idx=i))


# Create a copy of object_list to iterate over for selection
object_list_copy = copy.deepcopy(object_list)

for i,j in enumerate(object_list_copy):
    if j.next_ind is None:
        object_list.pop(i)

solutions = solve(object_list, CAPACITY)

day_indexes = []
for a in solutions:
    day_indexes.append(a.indexes)
    day_indexes.append([i for i in range(a.indexes[-1]+1, a.next_ind)])
    day_indexes.append(is_in_sublist(a.next_ind, org_indexes))
day_indexes = list(set(list(itertools.chain.from_iterable(day_indexes))))

organized_solutions = consec_val_list_split(day_indexes)

for b in organized_solutions:
    print(b[0], b[-1])

print(organized_solutions)

gui(solve, object_list)
