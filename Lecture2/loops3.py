class Loops3:

    user_input = input("Write something\n")
    count_digit = 0;
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for ch in user_input:
        if(ch.isdigit()):
            count_digit += 1
        print(ch.isupper())


    for i in range(len(user_input)):
        print(f"index {i} Char: {user_input[i]}") #prints which index
        if user_input[i] in vowels:
            print(f"index vowel at pos {[i]} -> {user_input[i]}")

    print(f"2nd index char: {user_input[1]}")  # prints index 2
    print(count_digit)


