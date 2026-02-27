class Table:
    num = 5
    for row in range(1, num + 1):
        for col in range(1, num + 1):
            value = row * col
            print(f"{value:4}", end="")
        print()







