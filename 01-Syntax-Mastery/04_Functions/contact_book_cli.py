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

def list_contacts():
    if not contacts:
        print("No contacts saved.")
        return

    print("\nAll Contacts:")
    for name, phone in contacts.items():
        print(f"{name} -> {phone}")


def menu():
    while True:
        print("""
1. Add Contact
2. Search Contact
3. Delete Contact
4. List Contacts
5. Exit
""")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()