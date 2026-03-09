class Exercise1:
    def run_operations(self):
        person = {"a":1, "b":2, "c":1, "d":3, "e":1}
        self.rev_lookup(1, person)

    def rev_lookup(self, val, dic):
        lst = []

        for key, vl in dic.items():
            if vl == val:
                lst.append(key)

        print(lst)





