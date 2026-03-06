import random

class ExerciseNext1:

    lst = []

    def _list_fill(self):
        while True:
            if len(self.lst) == 10:
                break
            random_number = random.randint(1, 10)
            self.lst.append(random_number)
        print(self.lst,"\n")

    def _for_list(self):
        for values in self.lst:
            print(values, end=" | ")
        print("\n")

    def _sum_list(self):
        total = 0
        for values in self.lst:
            total += values
        print(total,"\n")

    def _even_odd_list(self):
        amount_even = 0
        amount_odd = 0
        for values in self.lst:
            if values % 2 == 0:
                amount_even += 1
            else:
                amount_odd += 1
        print(amount_even,"\n")
        print(amount_odd,"\n")

    def _remove_odd_list(self):
        new_lst = self.lst.copy()
        for v in new_lst:
            if v % 2 != 0:
                self.lst.remove(v)
        print(new_lst)

    def _list_fill_new(self):
        lst_new = self.lst.copy()
        while True:
            if len(lst_new) == 20:
                break
            random_number = random.randint(0, 99)
            lst_new.append(random_number)
        print(lst_new,"\n")
        lst_new.sort()
        print(lst_new,"\n")

    def _same_list(self, a, b):
        return set(a) == set(b)

    def _sum_without_smallest(self):
        lst_new = self.lst.copy()
        total = 0
        temp = 101

        while len(lst_new) < 10:
            random_number = random.randint(1, 100)
            lst_new.append(random_number)
            total += random_number

            if random_number < temp:
                temp = random_number

        print(temp)
        print(total)

        return total - temp

    def _remove_min(self):
        lst_new = self.lst.copy()
        print(min(lst_new))

    def _remove_tuple_dupe(self):
        t_lst = [(1, 2), (5, 7), (1, 2), (4, 3), (1, 2)]
        seen = set()
        empty_lst = []
        for t in t_lst:
            if t not in seen:
                seen.add(t)
                empty_lst.append(t)
        print("Old tuple list: ",t_lst)
        print("New tuple list: ", empty_lst)

    def run_list_operations(self):
        self._remove_tuple_dupe()
        #self._list_fill()
        #self._remove_min()
        #self._sum_without_smallest()
        #a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
        #b = [11, 11, 7, 9, 16, 4, 1]
        #print(self._same_list(a, b))
        #self._list_fill_new()
        #self._for_list()
        #self._sum_list()
        #self._even_odd_list()
        #self._remove_odd_list()

