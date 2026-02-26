import statistics

class Loops2:
    name_first = input("first name\n")
    name_last = input("last name\n")
    numbers = []
    iInput = int(input("Enter score (-1 to stop)\n"))

    while iInput != -1:
        numbers.append(iInput)
        iInput = int(input("Enter score (-1 to stop)\n"))
    result = statistics.mean(numbers)
    print(result)
