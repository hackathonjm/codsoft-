class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'Phone Number': phone_number, 'Email': email, 'Address': address}
        print(f"Contact {name} added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, info in self.contacts.items():
                print(f"{name}: {info['Phone Number']}")

    def search_contact(self, query):
        results = []
        for name, info in self.contacts.items():
            if query.lower() in name.lower() or query in info['Phone Number']:
                results.append((name, info))
        return results

    def update_contact(self, name, field, new_value):
        if name in self.contacts:
            self.contacts[name][field] = new_value
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            query = input("Enter Name or Phone Number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("Search Results:")
                for name, info in results:
                    print(f"{name}: {info['Phone Number']}")
            else:
                print("No results found.")

        elif choice == '4':
            name = input("Enter Name to update: ")
            field = input("Enter field to update (Phone Number, Email, Address): ")
            new_value = input(f"Enter new {field}: ")
            contact_book.update_contact(name, field, new_value)

        elif choice == '5':
            name = input("Enter Name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

    