class UserInput:

    #num_input = int(input("Enter a number between 1-10"))
    #if num_input > 10:
    #    print(f"Your number is larger than 10: -> {num_input}")
    #elif 10 > num_input >= 0:
    #    print(f"Your number is smaller than 10: -> {num_input}")
    #elif num_input < 0:
    #    print(f"Your number is smaller than 0: -> {num_input}")


    while True:
        num_grade_input = int(input("Enter the score (0-100):"))
        if num_grade_input == 1:
            break
        if 90 <= num_grade_input <= 100:
            print(f"The letter grade is A: -> {num_grade_input}")
        elif 80 <= num_grade_input <= 89:
            print(f"The letter grade is B: -> {num_grade_input}")
        elif 70 <= num_grade_input <= 79:
            print(f"The letter grade is C: -> {num_grade_input}")
        elif 60 <= num_grade_input <= 69:
            print(f"The letter grade is D: -> {num_grade_input}")
        elif 60 > num_grade_input >= 0:
            print(f"The letter grade is F: -> {num_grade_input}")
        else:
            print("Wrong format input a number")


