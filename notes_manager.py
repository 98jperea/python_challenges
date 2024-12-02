import json

def save_note(note):
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    notes.append(note)
    
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def list_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            for idx, note in enumerate(notes, 1):
                print(f"{idx}. {note}")
    except FileNotFoundError:
        print("No notes found!")

if __name__ == "__main__":
    while True:
        print("\n1. Add Note\n2. List Notes\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            note = input("Enter your note: ")
            save_note(note)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")