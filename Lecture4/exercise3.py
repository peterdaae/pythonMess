class Exercise3:
    def user_input(self):
        list = []
        while True:
            if len(list) == 5:
                break
            user_input = int(input("Input an integer\n"))
            if user_input == 0:
                break
            list.append(user_input)
        return list

    def swap_first_last(self, list):
        list_swap = list.copy()
        first = list_swap[0]
        last = list_swap[-1]
        list_swap[0] = last
        list_swap[4] = first
        print(list_swap)

    def move_elements_right(self, list):
        list_move = list.copy()
        last = list_move[-1]
        for i in range(len(list_move) - 1, 0, -1):
            list_move[i] = list_move[i -1]
        list_move[0] = last
        print(list_move)

    def check_even(self, list):
        list_even = list.copy()
        for i, v in enumerate(list_even):
            if v % 2 == 0:
                list_even[i] = 0
            else:
                continue
        print(list_even)

    def rem_middle(self, list):
        list_middle = list.copy()
        middle_index = (len(list_middle)) // 2
        print(f"before removal: {list_middle}")
        list_middle.pop(middle_index)
        print(f"after removal: {list_middle}")