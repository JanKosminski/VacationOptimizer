import pandas as pd


class Vacation:

    def __init__(self, nums):
        self.dist2prev = int()
        self.dist2next = int()
        self.next_ind = int()
        self.prev_ind = int()
        self.days = len(nums)
        self.indexes = nums


    def check_dist(self, whole_list: list[int]):
        result = []
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