import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(search_age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [age for age in users if age["age"] == search_age]

    for user in filtered_users:
        print(user)

def filter_users_by_mail(search_mail):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [mail for mail in users if mail["email"] == search_mail]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/age/mail): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    elif filter_option == "mail":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_mail(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
