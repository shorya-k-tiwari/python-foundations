"""
Simple contact book 

Simple command-line contact manager using functions and dictionary storage
"""

contacts = {}

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone number: ").strip()    
    if name in contacts:
        print("That contact already exists, updating the number")
    contacts[name] = phone
    print("Saved")

def search_contact():
    name = input("Search name: ").strip()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print("Couldn't find that contact")

def delete_contact():
    name = input("Delete name: ").strip()
    if name in contacts:
        del contacts[name]
        print("Deleted")
    else:
        print("Couldn't find that contact")

def list_contacts():
    if not contacts:
        print("No contacts yet")
        return

    print("\nContacts:")
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

        choice = input("Pick an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            print("Closing contact book")
            break
        else:
            print("That option is not valid")

if __name__ == "__main__":
    menu()