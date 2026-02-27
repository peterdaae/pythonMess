class Palindrome:
    """
    string = "tacocat"
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            print(f"Not Palindrome ---> {string}")
            break

    else:
        print(f"Palindrome ---> {string}")
    """
    #Obviously an easier way wtf is this ^

    easier_string = "level"
    reversed_string = "".join(reversed(easier_string)) #"".join -> returns reversed iterator to back into string before comparing
    if reversed_string == easier_string:
        print("Palindrome")
    else:
        print("Not Palindrome")

