import csv

def listAll():
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)

        users_found = False
        for i, row in enumerate(reader,1):
            if(row):
                print(f"{i} : {row[0]} - {row[1]} - {row[2]}")
                users_found = True
        if not users_found:
            print("No users found")

def signUp():
    print("\nWelcome, new member! Please sign up.")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    new_user = {
        "username": name, 
        "email": email, 
        "password": password
    }

    # Log created user info
    # print(new_user)

    try:
        with open('users.csv', 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Email", "Password"])
    except FileExistsError:
        pass

    with open('users.csv', 'r') as file:
        readExistingUser = csv.reader(file)
        for existingUser in readExistingUser:
            if existingUser[0] == name and existingUser[1]:
                print("Username or email already exists.")
                return
    
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, password])
        print("Sign-up successful! Your data has been saved.\n")

def signIn():
    print("\nWelcome back! Please sign in to your account.")
    signInEmail = input("Email: ")
    signInPassword = input("Password: ")

    with open('users.csv', 'r') as file:

        getInfo = csv.reader(file)

        for data in getInfo:
            if data[1] == signInEmail and data[2] == signInPassword:
                print(f"Welcome back, {data[0]}")

def exitApp():
    print("See you next time!")

def menu():
    print("\nAUTHENTICATION")
    print("1. Sign up")
    print("2. Sign in")
    print("3. All Users")
    print("4. Exit")
    try:
        choice = int(input("Choose your option [1-4]: "))
        return choice
    except ValueError:
        print("Please enter a number between 1 and 4.")
        return None

while True:
    inputMenu = menu()
    match inputMenu:
        case 1:
            signUp()
        case 2:
            signIn()
        case 3:
            listAll()
        case 4:
            exitApp()
            break
        case _:
            print("Please try again!\n")
