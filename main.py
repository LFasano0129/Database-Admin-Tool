# function to import database from UD.txt file
def import_database():
    database = {}

    with open("UD.txt", "r") as file:
        header = file.readline().strip()
        expected_header = "First Name,Last Name,Username,Password"

        if header != expected_header:
            print("Invalid file format. Expected header:", expected_header)
            return database

        for line in file:
            line = line.strip()
            if line:
                data = line.split(",")
                if len(data) == 4:
                    first_name, last_name, username, password = data
                    database[username] = [first_name, last_name, username, password]

    return database


# function to display available operations
def display_menu():
    print("A: Search by last name")
    print("B: Search by first name")
    print("C: Search by username")
    print("D: Display all users alphabetically by First name")
    print("E: Display all users alphabetically by Last name")
    print("F: Insert a user\n")


# function to print all data for a user from the database
def print_user_data(user_data):
    first_name, last_name, username, password = user_data
    print(f"\nFirst Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Username: {username}")
    print(f"Password: {password}\n")


# function to search and display data for a user by last name
def search_ln(database):
    last_name = input("Enter user's last name: ")

    found = False
    for user_data in database.values():
        if user_data[1] == last_name:
            print_user_data(user_data)
            found = True
            break

    if not found:
        print("Not found")


# function to search and display data for a user by first name
def search_fn(database):
    first_name = input("Enter user's first name: ")

    found = False
    for user_data in database.values():
        if user_data[0] == first_name:
            print_user_data(user_data)
            found = True
            break

    if not found:
        print("Not found")


# function to search and display data for a user by username
def search_un(database):
    username = input("Enter username: ")

    found = False
    for user_data in database.values():
        if user_data[2] == username:
            print_user_data(user_data)
            found = True
            break

    if not found:
        print("Not found")


# function to display users in alphabetical order by first or last name
def output(database, sort_key):
    sorted_users = sorted(database.values(), key=lambda x: x[sort_key])
    for user_data in sorted_users:
        print_user_data(user_data)


# function to insert data into the database
def insert_user(database):
    user_info = input("Enter user info in the following format: First name,last name,username,password: ")
    first_name, last_name, username, password = user_info.strip().split(",")

    # insert the user data into the database dictionary
    database[username] = [first_name, last_name, username, password]

    # save the updated dictionary data into the database file (UD.txt)
    with open("UD.txt", "w") as file:
        file.write("First Name,Last Name,Username,Password\n")

        for user_data in database.values():
            first_name, last_name, username, password = user_data
            file.write(f"{first_name},{last_name},{username},{password}\n")


# main function to call operation functions
def main():
    database = import_database()
    while True:
        display_menu()
        choice = input("Enter your choice (A, B, C, D, E, F) or 'X' to quit: ")

        if choice == "A":
            search_ln(database)  # call function to search by last name
        elif choice == "B":
            search_fn(database)  # call function to search by first name
        elif choice == "C":
            search_un(database)  # call function to search by username
        elif choice == "D":
            output(database, sort_key=0)  # display all users in alphabetical order by first name
        elif choice == "E":
            output(database, sort_key=1)  # display all users in alphabetical order by last name
        elif choice == "F":
            insert_user(database)  # insert a user
        elif choice == "X":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
