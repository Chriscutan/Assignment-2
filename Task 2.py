import re

def register():
    reg_email = input("Enter your Email: ")
    reg_password = input("Enter your Password: ")

    email_pattern = '^[a-z]+@+[a-z0-9]+\\.+[a-z]'
    email_valid = re.match(email_pattern, reg_email)

    password_pattern = '[A-Z]+[a-z]+[!@#$&]+[0-9]'
    password_valid = re.match(password_pattern, reg_password)

    if email_valid and password_valid and 5 < len(reg_password) < 16:
        with open("user.txt", "a") as f:
            f.write(reg_email + " ")
            f.write(reg_password + " ")
        print("Registered Successfully")
        home()
    else:
        print("Data Invalid")


def login():
    user_email = input("Enter your Email: ")
    user_password = input("Enter your Password: ")

    usersinfo = []
    with open("user.txt", "r") as f:
        for line in f:
            line = line.split(" ")
        for i in line:
            usersinfo.append(i)

    if user_email and user_password in usersinfo:
        print("Logged in Successfully")
    else:
        print("You are not a registered user. Please register yourself")
        error_choice = input("Type 'r' to register yourself")
        error_choice = error_choice.lower()
        if error_choice == 'r':
            register()

def forgot_password():
    user_email = input("Enter your Email: ")

    key = []
    value = []
    users_dict = {} 
    with open("user.txt", "r") as f:
        for line in f:
            line = line.split(" ")
        for i in range(0, len(line) - 1, 2):
            key.append(line[i])
        for i in range(1, len(line), 2):
            value.append(line[i])
        users_dict = dict(zip(key, value))
        if user_email in users_dict:
            print("Your Password: " + users_dict[user_email])
            home()
        else:
            print("You need to register yourself!!")
            home()
    
def home():
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")

    while True:
        choice = int(input("Choose one option: "))
        if choice in [1, 2, 3]:
            break

    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        forgot_password()


home()
