class CheckUser:

    def checkInput(self):
        username = input("Enter your username:")
        password = input("Enter your password:")
        password_length = len(password) #Checks length of string
        hidden_password = "*" * password_length
        print(f"Hi {username}. Your password is: {hidden_password} and is {password_length} characters long")

