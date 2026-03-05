class Exercise5:
    def remove_dupes(self, l1, l2):
        new_lst = l1 + l2
        empty_lst = []
        for dupe in new_lst:
            if dupe not in empty_lst:
                empty_lst.append(dupe)
        split_middle = len(empty_lst) // 2
        first = empty_lst[:split_middle]
        second = empty_lst[split_middle:]

        print(first)
        print(second)