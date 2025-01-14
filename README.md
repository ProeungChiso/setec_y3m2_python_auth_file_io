# Authentication System Application

This is a simple command-line application that allows users to sign up, sign in, and view all registered users stored in a CSV file. The application provides basic authentication functionality using a CSV file as the data store.

## Features

1. **Sign up** - New users can create an account by providing their username, email, and password. The system checks for duplicate usernames and emails.
2. **Sign in** - Existing users can log in using their email and password.
3. **View All Users** - A list of all registered users is displayed, showing their username, email, and password.
4. **Exit** - The user can exit the application.

## Requirements

- Python 3.x
- CSV file to store user data (`users.csv`)

## How to Use

1. **Run the Application**
   - Execute the Python script to start the application. It will show a menu with the following options:
     1. Sign up
     2. Sign in
     3. View all users
     4. Exit the application
     
2. **Sign Up**
   - Choose option `1` to create a new account. You'll be prompted to enter a username, email, and password. The system will check if the username and email already exist in the `users.csv` file.

3. **Sign In**
   - Choose option `2` to log in with an existing account. Enter your email and password, and if they match the records in the CSV file, you will be welcomed back.

4. **View All Users**
   - Choose option `3` to view a list of all registered users in the `users.csv` file.

5. **Exit**
   - Choose option `4` to exit the application.

## Code Overview

- **`listAll()`**: Reads the `users.csv` file and displays a list of all users.
- **`signUp()`**: Allows new users to sign up by saving their details in the `users.csv` file after checking for duplicates.
- **`signIn()`**: Validates user credentials against the data in the `users.csv` file.
- **`exitApp()`**: Displays a message when the user chooses to exit the application.
- **`menu()`**: Displays the main menu and allows the user to choose an action.

## `users.csv` File Format

The `users.csv` file stores user information in the following format:

| Username  | Email            | Password |
|-----------|------------------|----------|
| user1     | user1@mail.com    | password1|
| user2     | user2@mail.com    | password2|

### Note:
- The application creates the `users.csv` file if it doesn't already exist.
- The first time the file is created, it includes headers: "Username", "Email", and "Password".

