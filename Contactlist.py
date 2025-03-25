import json
import os

# Define the file name where contacts will be saved
CONTACTS_FILE = 'contacts.json'

# Function to load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to display all contacts
def view_contacts(contacts):
    if contacts:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contacts found.")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    save_contacts(contacts)
    print(f"Contact for {name} added successfully!")

# Function to search contacts by name or phone
def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = {name: details for name, details in contacts.items() if search_term.lower() in name.lower() or search_term in details['phone']}
    
    if found_contacts:
        print("\n--- Search Results ---")
        for name, details in found_contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contacts found matching your search.")

# Function to update an existing contact
def update_contact(contacts):
    name = input("Enter the name of the contact you want to update: ")
    
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")
        
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        save_contacts(contacts)
        print(f"Contact for {name} updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully!")
    else:
        print("Contact not found.")

# Main function to display menu and handle user choices
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
