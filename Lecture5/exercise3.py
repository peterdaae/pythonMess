class Exercise3:
    def read_input(self):
        a = input("Enter first word: \n")
        b = input("Enter second word: \n")
        check = True

        for ch in a:
            if ch not in b:
                check = False
                break

        if check:
            print("ANAGRAM")

        else:
            print("NOT ANAGRAM")




