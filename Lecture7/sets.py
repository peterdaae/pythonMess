class Sets:
    def testSet(self):
        fruits = {"banana", "apple", "pineapple"} #Declares set of fruits
        int_array = [1, 2, 3, 4, 5, 1, 1, 5, 3] #Simple array integers
        set1 = set() #creates empty set
        set2 = set(int_array) #puts int_array into
        #stores unique values, removes duplicates
        #Sets are mutable collections of unique values

        print(fruits)
        print(len(fruits)) #Checks length of elements
        print("apple" in fruits) #Checks boolean if item is inside set returns true/false

        fruits.add("kiwi") #adds item to set, cannot add exisiting item
        fruits.remove("kiwi") #Remove element if exist in set, will throw exception if not exist
        #Prefered & convenient
        fruits.discard("") #Removes element if exist in set, will not throw exception if not exist
        fruits.clear() #clears entire set

        for fruit in sorted(fruits): #Sorted function used returns a list, not a set
            print(fruit)

        print("set contains: ")
        for fruit in fruits: #Cannot access elements by position so iterate through individual elementes
            print(fruit)

        #Subsets
        fruits_general = {"banana", "apple"}
        fruits_exotic = {"banana", "apple", "dragonfruit"}
        fruits_northern = {"banana", "kiwi", "mango"}

        if fruits_general.issubset(fruits_exotic):
            print("all fruits in exotic is in general")

        if not fruits_general.issubset(fruits_northern):
            print("some fruits are part of set")

        #Union, removes duplicates
        inEither = fruits_exotic.union(fruits_general)

        #Intersection, returns new set that contains elements that are in both sets
        #Difference, returns new set that contains elements that are in one but not the other




