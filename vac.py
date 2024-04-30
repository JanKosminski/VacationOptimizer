from functions import is_in_sublist, consec_val_list_split


class Vacation:

    def __init__(self, nums, whole_list):
        self.dist2prev = None
        self.dist2next = None
        self.next_ind = None
        self.prev_ind = None
        self.days = len(nums)
        self.indexes = nums
        self.check_dist(whole_list)
        self.efficiency1 = None
        self.efficiency2 = None
        self.check_total_day_count(consec_val_list_split(whole_list))

    def check_dist(self, whole_list: list[int]):
        firs_ind = (whole_list.index(self.indexes[0]))
        try:
            if len(self.indexes) > 1:
                last_ind = whole_list.index(self.indexes[-1])
                # calculate distance to next and previous one in whole list
                t2prev = abs(whole_list[abs(firs_ind - 1) % len(whole_list)] - self.indexes[0]) - 1
                t2next = abs(self.indexes[-1] - whole_list[last_ind + 1]) - 1
            else:
                # dumb but it will crash without that assignment
                last_ind = firs_ind
                t2prev = abs(whole_list[firs_ind - 1] - self.indexes[0]) - 1
                t2next = abs(self.indexes[0] - whole_list[firs_ind + 1]) - 1
        # catches error when there is no next thing on list
        except IndexError:
            # returns index of nearest previous free day and distance
            self.dist2prev = t2prev
            self.prev_ind = whole_list[firs_ind]
        else:
            # returns index of previous free day and distance then distance to next and index of next free day
            self.dist2prev = t2prev
            self.prev_ind = whole_list[firs_ind]
            self.dist2next = t2next
            self.next_ind = whole_list[last_ind]

    def check_total_day_count(self, consecutive_indexes_list):
        sum_w_prev = self.days + len(is_in_sublist(self.prev_ind, consecutive_indexes_list)) + self.dist2prev
        if self.prev_ind is not None:
            self.efficiency1 = self.dist2prev / sum_w_prev
        if self.next_ind is not None:
            sum_w_next = self.days + len(is_in_sublist(self.next_ind, consecutive_indexes_list)) + self.dist2next
            self.efficiency2 = self.dist2next / sum_w_next
