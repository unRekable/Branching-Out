import json

"""
This script filters a list of users from a JSON file
based on name, age, or email address.
"""


def filter_users_by_name(name):
    """
    Filters users from 'users.json' by name (case-insensitive).

    Args:
        name (str): The name to filter by.
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Error: The file 'users.json' was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The file 'users.json' contains invalid JSON.")
        return

    filtered_users = [
        user for user in users if user.get("name", "").lower() == name.lower()
    ]

    if not filtered_users:
        print(f"No users found with the name '{name}'.")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_age(search_age):
    """
    Filters users from 'users.json' by age.

    Args:
        search_age (int): The age to filter by.
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Error: The file 'users.json' was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The file 'users.json' contains invalid JSON.")
        return

    filtered_users = [
        user for user in users if isinstance(user.get("age"), int) and user["age"] == search_age
    ]

    if not filtered_users:
        print(f"No users found with the age '{search_age}'.")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_mail(search_mail):
    """
    Filters users from 'users.json' by email address (case-insensitive).

    Args:
        search_mail (str): The email address to filter by.
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Error: The file 'users.json' was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The file 'users.json' contains invalid JSON.")
        return

    filtered_users = [
        user for user in users if user.get("email", "").lower() == search_mail.lower()
    ]

    if not filtered_users:
        print(f"No users found with the email address '{search_mail}'.")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (name/age/mail): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        if name_to_search:
            filter_users_by_name(name_to_search)
        else:
            print("No name entered.")
    elif filter_option == "age":
        age_input = input("Enter an age to filter users: ").strip()
        if age_input.isdigit():
            age_to_search = int(age_input)
            filter_users_by_age(age_to_search)
        else:
            print("Invalid age input. Please enter a number.")
    elif filter_option == "mail":
        email_to_search = input("Enter an email to filter users: ").strip()
        if email_to_search:
            filter_users_by_mail(email_to_search)
        else:
            print("No email entered.")
    else:
        print("Filtering by that option is not yet supported.")