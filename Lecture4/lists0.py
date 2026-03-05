class Lists0:
    def list(self):
        arr = [24, 35, 11, 65, 9, 93, 45]
        # arr.insert(1, 36) to insert new element at index

        #subscript aka last element in list
        last_int = arr[-1]

        #Position and elements of array
        for i in range(len(arr)):
            print(i , arr[i])

        print("----------")

        #Only prints elements
        for element in arr:
            print(element)

        print("----------")
        print(f"Last element in list: {last_int}")
        #Add new element to list
        arr.append(999)
        last_int_new = arr[-1]
        print(f"New last element in list: {last_int_new}")

        #Check if in list
        if 9 in arr:
            print("true")
        else:
            print("false")

        #Check if in list and what index
        index_number = arr.index(9)
        print(index_number)


