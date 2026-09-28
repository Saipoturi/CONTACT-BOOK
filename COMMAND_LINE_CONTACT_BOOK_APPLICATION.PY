# COMMAND LINE CONTACT BOOK APPLICATION
# File to store contact details
filename = "contacts.txt"
# Function to add a new contact
def add_contact():
    print("\n----- Add New Contact -----")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    if name == "" or phone == "" or email == "":
        print("All fields are required!")
        return
    # Save contact details in text file
    with open(filename, "a") as file:
        file.write(name + "," + phone + "," + email + "\n")
    print("\nContact added successfully!")
    
# Function to view all contacts
def view_contacts():
    print("\n----- All Contacts -----")
    try:
        with open(filename, "r") as file:
            contacts = file.readlines()
        if len(contacts) == 0:
            print("No contacts found!")
            return
        for contact in contacts:
            details = contact.strip().split(",")
            if len(details) == 3:
                print("-------------------------")
                print("Name  :", details[0])
                print("Phone :", details[1])
                print("Email :", details[2])
        print("-------------------------")
    except FileNotFoundError:
        print("No contacts found! Please add a contact first.")

# Function to search for a contact
def search_contact():
    print("\n----- Search Contact -----")
    search_name = input("Enter name to search: ").strip().lower()
    if search_name == "":
        print("Please enter a name!")
        return
    found = False
    try:
        with open(filename, "r") as file:
            contacts = file.readlines()
        for contact in contacts:
            details = contact.strip().split(",")
            if len(details) == 3:
                name = details[0]
                phone = details[1]
                email = details[2]
                if search_name in name.lower():
                    print("\nContact Found!")
                    print("-------------------------")
                    print("Name  :", name)
                    print("Phone :", phone)
                    print("Email :", email)
                    print("-------------------------")
                    found = True
        if not found:
            print("Contact not found!")
    except FileNotFoundError:
        print("No contacts available! Please add a contact first.")

# Main program
def main():
    while True:
        print("\n==============================")
        print("       CONTACT BOOK")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        print("==============================")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("\nThank you for using Contact Book!")
            print("Program terminated.")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, 3, or 4.")
            
# Execute the program
if __name__ == "__main__":
    main()