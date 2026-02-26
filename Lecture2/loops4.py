import statistics

class Loops4:

    dset = set()

    while True:
        user_input = input("Write a number (or 'exit' to exit):\n")

        if user_input == "exit":
            break

        value = float(user_input)
        dset.add(value)

    print("Average:", statistics.mean(dset))
    print("Minimum:", min(dset))
    print("Maxium:", max(dset))
    range = min(dset) - max(dset)
    print(f"Range {range}")


