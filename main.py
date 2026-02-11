# User Management System in Python
# Author: Rodrigo Monsalve Vasquez
# Description: Simple console-based user management system with JSON persistence

import json
import os

DATA_FILE = "users.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def list_users(users):
    if not users:
        print("\nNo users registered.\n")
        return
    print("\nRegistered users:")
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user['name']} - {user['email']}")
    print()

def add_user(users):
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty.")
        return

    for user in users:
        if user["email"].lower() == email.lower():
            print("A user with this email already exists.")
            return

    users.append({"name": name, "email": email})
    save_users(users)
    print("User added successfully.")

def find_user(users):
    query = input("Enter name or email to search: ").strip().lower()
    results = [u for u in users if query in u["name"].lower() or query in u["email"].lower()]

    if not results:
        print("No users found.")
        return

    print("\nSearch results:")
    for user in results:
        print(f"- {user['name']} ({user['email']})")
    print()

def delete_user(users):
    list_users(users)
    if not users:
        return
    try:
        index = int(input("Enter user number to delete: "))
        if 1 <= index <= len(users):
            removed = users.pop(index - 1)
            save_users(users)
            print(f"User deleted: {removed['name']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    print("==== USER MANAGEMENT SYSTEM ====")
    print("1. List users")
    print("2. Add user")
    print("3. Find user")
    print("4. Delete user")
    print("5. Exit")

def main():
    users = load_users()
    while True:
        menu()
        option = input("Choose an option: ").strip()
        if option == "1":
            list_users(users)
        elif option == "2":
            add_user(users)
        elif option == "3":
            find_user(users)
        elif option == "4":
            delete_user(users)
        elif option == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
