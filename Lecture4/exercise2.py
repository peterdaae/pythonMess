class Exercise2:
    def user_input(self):
        list = []
        while True:
            user_input = int(input("Input an integer\n"))
            if user_input == 0:
                break
            list.append(user_input)
        return list


    def list_display(self, list):
        for i in reversed(list):
            print(i)
