from functions import *
from vac import *
import copy
CAPACITY = 11

lsit = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
whole_index_list = indexes_of_val(lsit)
print(whole_index_list)

org_indexes = consec_val_list_split(whole_index_list)
org_indexes.sort(key=len, reverse=True)
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
    temp = [a.indexes[0], is_in_sublist(a.next_ind, org_indexes)[-1]]
    day_indexes.append(temp.copy())
    temp.clear()

print(day_indexes)
