class Exercise4:
    def split_replace(self):
        lst = [1, 4, 9, 16, 25, 36]
        middle_lst = len(lst) // 2
        first_half = lst[:middle_lst]
        second_half = lst[middle_lst:]
        new_lst = second_half + first_half
        print(new_lst)
