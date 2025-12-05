# Global constant for the file path


# The main list where all contacts will be stored in memory
# Example structure: [{'name': 'Alice', 'phone': '123-4567', 'email': 'a@example.com'}]


import json
import os
from typing import List, Dict, Any # Type Hinting

DATA_FILE = "contacts.txt"
CONTACTS: List[dict[str, str]] = [] # Update type hint for clarity

## 💾 Data Management Functions

def load_contacts():
    """Loads contact data from the JSON file."""
    # Checks if the file exists (Clean Error Handling)
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        print(f"File '{DATA_FILE}' not found or empty. Starting with no contacts.")
        return 
    
    # Use a Context Manager (with) for safe file opening
    try:
        with open(DATA_FILE, 'r') as f:
            global CONTACTS
            CONTACTS = json.load(f)
        print(f"Loaded {len(CONTACTS)} contacts.")
    except json.JSONDecodeError:
        # Handle case where the file is corrupted (Errors + Debugging)
        print(f"Error: Could not read valid JSON from {DATA_FILE}. Data might be corrupted.")
    except Exception as e:
        # Catch any other unexpected I/O errors
        print(f"An unexpected error occurred while loading: {e}")

def save_contacts():
    """Saves the current CONTACTS list on the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(CONTACTS, f, indent=4) # indent=4 is for clean code/readability
        print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")

## Core Application Functions

def add_contact():
    """Prompts user for contact details and adds to the list."""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    if not name or not phone:
        print("Name and Phone are required fields. Contact not added.")
        return
    
    new_contact = {'name': name, 'phone': phone, 'email': email}
    CONTACTS.append(new_contact)
    save_contacts()

def view_contacts():
    """Displays all contacts in a formatted list."""
    if not CONTACTS:
        print("The contact book is empty")
        return
    
    print("\n--- All Contacta ---")
    # Loops and Enumerate (efficient looping)
    for i, contact in enumerate(CONTACTS, 1):
        print(f"[{i}] Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
    print("--------------------")

def search_contacts():
    """Prompts for a search term and displays matching contacts."""
    term = input("Enter search term (name or phone): ").strip().lower()
    if not term:
        print("Search term cannot be empty.")
        return
    
    found_contacts =[]
    # Loops and Conditional Logic
    for contact in CONTACTS:
        # Check if the term is in the name or phone number
        if term in contact['name'].lower() or term in contact['phone']:
            found_contacts.append(contact)

        if found_contacts:
            print(f"\n--- Found {len(found_contacts)} Contacts ---")
            for contacts in found_contacts:
                print(f"NAME: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
            print("--------------------")
        
        else:
            print(f"No contacts found matching '{term}'.")

def delete_contact():
    """Prompts for an index and deletes the corresponding contact. """
    view_contacts()
    if not CONTACTS:
        return
    
    index_str = input("Enter the number of the contact to delete (or 'c to cancle): ").strip()
    if index_str.lower() == 'c':
        print("Deletion cancelled.")
        return
    
    # Errors + Debugging (Input Validation)
    try:
        index = int(index_str ) - 1

        if 0 <= index < len(CONTACTS):
            delete_contact = CONTACTS.pop(index) # List mutation
            print(f"Deleted contact: {delete_contact['name']}")
            save_contacts()

        else:
            print("Invalide number. Please choose a number from the list. ")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    ## Main Excecution

def display_menu():
        """Displays the interactive menu."""
        print("\n\n--- Contact Manager Menu ---")
        print("[1] Add New Contact")
        print("[2] View All Contacts")
        print("[3] Search Contacts")
        print("[4] Delete Contact")
        print("[5] Exit")
        print("----------------------------")
    
def main():
        """The main entry point of the application. """
        print("Starting Contact Manager...")
        load_contacts() # Load data at startup

        # Infinite Loop (Program keeps rumming until the user quits)
        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                add_contact()
            elif choice == '2':
                view_contacts()
            elif choice == '3':
                search_contacts()
            elif choice == '4':
                delete_contact()
            elif choice == '5':
                print("Existing Contact Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5. ")

# Standard Python entry point (Clean Code)
if __name__ == "__main__":
    main()