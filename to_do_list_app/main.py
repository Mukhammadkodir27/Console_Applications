# Lets create a todo list app

# option to sign up, login

def sign_up():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    username = input("Choose your username: ")
    password = input("Set a password: ")

    if username not in user_usernames.keys():
        user_names.append(name)
        user_surnames.append(surname)
        user_usernames[username] = password
        print("Sign up success")
    else:
        print("Please choose another username. This one already exists!")


def log_in():
    print("Please provide your username and password")
    username = input("username: ")
    password = input("password: ")

    if username in user_usernames and user_usernames[username] == password:
        print("login success")
    else:
        print("invalid username or password")


user_names = []
user_surnames = []
user_usernames = {}

print("Please choose the following: ")
print("Press 1 to sign up")
print("Press 2 to login")
option = int(input("Value: "))

if option == 1:
    sign_up()
    log_in()
elif option == 2:
    log_in()
else:
    print("Invalid option")
