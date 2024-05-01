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
        # check length
        first_ind = (whole_list.index(self.indexes[0]))
        if len(self.indexes) > 1:
            last_ind = whole_list.index(self.indexes[-1])
        else:
            last_ind = first_ind
        # check position
        if first_ind != 0:
            self.prev_ind = whole_list[first_ind - 1]
            self.dist2prev = abs(self.prev_ind - self.indexes[0]) - 1
        if last_ind != (len(whole_list) - 1):
            self.next_ind = whole_list[last_ind + 1]
            self.dist2next = abs(self.indexes[-1] - self.next_ind) - 1

    def check_total_day_count(self, consecutive_indexes_list):
        if self.prev_ind is not None:
            sum_w_prev = self.days + len(is_in_sublist(self.prev_ind, consecutive_indexes_list)) + self.dist2prev
            self.efficiency1 = self.dist2prev / sum_w_prev
        if self.next_ind is not None:
            sum_w_next = self.days + len(is_in_sublist(self.next_ind, consecutive_indexes_list)) + self.dist2next
            self.efficiency2 = self.dist2next / sum_w_next
