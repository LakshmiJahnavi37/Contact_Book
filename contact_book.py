FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact saved successfully!")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n--- Contact List ---")
            for line in file:
                name, phone, email = line.strip().split(",")
                print("Name :", name)
                print("Phone:", phone)
                print("Email:", email)
                print("-------------------")
    except FileNotFoundError:
        print("No contacts found.")


def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")

                if search_name in name.lower():
                    print("\nContact Found")
                    print("Name :", name)
                    print("Phone:", phone)
                    print("Email:", email)
                    found = True
                    break

        if not found:
            print("Contact not found.")

    except FileNotFoundError:
        print("No contacts found.")


def delete_contact():
    delete_name = input("Enter name to delete: ").lower()
    contacts = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")

                if delete_name == name.lower():
                    found = True
                else:
                    contacts.append(line)

        if found:
            with open(FILE_NAME, "w") as file:
                for contact in contacts:
                    file.write(contact)

            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    except FileNotFoundError:
        print("No contacts found.")


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


main()
