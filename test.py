from vac import *
from functions import *


lsit = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]

whole_index_list = indexes_of_val(lsit)

print(whole_index_list)

org_indexes = consec_val_list_split(whole_index_list)
org_indexes.sort(key=len, reverse=True)

object_list = []
for it in org_indexes:
    object_list.append(Vacation(nums=it, whole_list=whole_index_list))



def efficiency(object_list_, index_list_2d):
    for j in object_list:
        if j.prev_ind is not None:
            sum_w_prev = len(j.indexes) + len(is_in_sublist(j.prev_ind, index_list_2d)) + j.dist2prev
            j.efficiency1 = j.dist2prev / sum_w_prev
        if j.next_ind is not None:
            sum_w_next = len(j.indexes) + len(is_in_sublist(j.next_ind, index_list_2d)) + j.dist2next
            j.efficiency2 = j.dist2next / sum_w_next


efficiency(object_list, org_indexes)

for j in object_list:
    print(j.prev_ind, j.dist2prev, j.next_ind, j.dist2next, j.efficiency1, j.efficiency2)
