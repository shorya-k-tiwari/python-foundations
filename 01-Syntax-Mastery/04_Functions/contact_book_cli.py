"""
Contact Book CLI
Simple command-line contact manager using functions and dictionary storage
"""

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    
    if name in contacts:
        print("Contact already exists. Updating number.")
    contacts[name] = phone
    print("Contact saved.")


def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

