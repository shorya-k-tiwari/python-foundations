"""
Simple Note App

Menu-driven CLI note manager
"""

def add_note(notes):
    text = input("Enter note: ").strip()
    if text:
        notes.append(text)
        print("Note added")
    else:
        print("Empty note not saved")

def view_notes(notes):
    if not notes:
        print("No notes available")
        return
    print("\nYour Notes:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")

def delete_note(notes):
    view_notes(notes)
    if not notes:
        return
    try:
        index = int(input("Enter note number to delete: "))
        if 1 <= index <= len(notes):
            removed = notes.pop(index - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number")

def main():
    notes = []
    while True:
        print("\n--- Note App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            print("BYE BYE!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()