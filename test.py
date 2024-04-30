from vac import *
from functions import *


lsit = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]

whole_index_list = indexes_of_val(lsit)
print(whole_index_list)

org_indexes = consec_val_list_split(whole_index_list)
org_indexes.sort(key=len, reverse=True)
print(org_indexes)

object_list = []
for it in org_indexes:
    object_list.append(Vacation(nums=it, whole_list=whole_index_list))

for j in object_list:
    print(j.prev_ind, j.dist2prev, j.next_ind, j.dist2next, j.efficiency1, j.efficiency2)
