class Vacation:

    def __init__(self, nums, whole_list, idx):
        self.value = 0
        self.dist2next = None
        self.next_ind = None
        self.prev_ind = None
        self.days = len(nums)
        self.indexes = nums
        self.selected = False  # Newly added attribute to track selection
        self.check_dist(whole_list)
        self.idx = idx

    def check_dist(self, whole_list: list[int]):
        # check length
        first_ind = (whole_list.index(self.indexes[0]))
        if len(self.indexes) > 1:
            last_ind = whole_list.index(self.indexes[-1])
        else:
            last_ind = first_ind
        # check if it is not last on the list
        if last_ind != (len(whole_list) - 1):
            self.next_ind = whole_list[last_ind + 1]
            self.dist2next = self.next_ind - self.indexes[-1] - 1
        if self.next_ind is not None:
            self.value = self.days + self.dist2next


class Node:
    def __init__(self):
        self.ub = 0  # Upper bound
        self.lb = 0  # Lower bound
        self.level = 0  # Level in the decision tree
        self.flag = False  # Flag to indicate if the item is selected or not
        self.tv = 0  # Total value of selected items
        self.tw = 0  # Total weight of selected items
