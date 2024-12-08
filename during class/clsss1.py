class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_contact(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print("-" * 20)


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        for contact in self.contacts:
            contact.display_contact()


# Create instances of Contact
contact1 = Contact("Alice Smith", "alice@example.com", "123-456-7890")
contact2 = Contact("Bob Johnson", "bob@example.com", "987-654-3210")

# Create an instance of ContactManager and add contacts
manager = ContactManager()
manager.add_contact(contact1)
manager.add_contact(contact2)

# Display all contacts
manager.list_contacts()