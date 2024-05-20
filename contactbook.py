import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Label, Entry, Button
import json

contacts_file = "contacts.json"

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open(contacts_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open(contacts_file, "w") as file:
        json.dump(contacts, file, indent=4)

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = load_contacts()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack(side=tk.LEFT, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.populate_listbox()

        self.add_button = tk.Button(self.root, text="Add Contact", width=20, command=self.add_contact)
        self.add_button.pack(pady=5)
        
        self.view_button = tk.Button(self.root, text="View Contact", width=20, command=self.view_contact)
        self.view_button.pack(pady=5)
        
        self.search_button = tk.Button(self.root, text="Search Contact", width=20, command=self.search_contact)
        self.search_button.pack(pady=5)
        
        self.update_button = tk.Button(self.root, text="Update Contact", width=20, command=self.update_contact)
        self.update_button.pack(pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Contact", width=20, command=self.delete_contact)
        self.delete_button.pack(pady=5)
        
    # Populate the listbox with contact names only
    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, contact['name'])

    # Add a new contact
    def add_contact(self):
        self.contact_window = Toplevel(self.root)
        self.contact_window.title("Add Contact")

        Label(self.contact_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = Entry(self.contact_window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.contact_window, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = Entry(self.contact_window)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.contact_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = Entry(self.contact_window)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.contact_window, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = Entry(self.contact_window)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        Button(self.contact_window, text="Add", command=self.save_new_contact).grid(row=4, column=0, columnspan=2, pady=10)

    # Save the new contact
    def save_new_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone and email and address:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            save_contacts(self.contacts)
            self.populate_listbox()
            self.contact_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please enter all details.")

    # View selected contact details
    def view_contact(self):
        selected_contact_index = self.listbox.curselection()
        if selected_contact_index:
            contact = self.contacts[selected_contact_index[0]]
            messagebox.showinfo("Contact Details", f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to view.")

    # Search for contacts by name or phone number
    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
        if query:
            results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
            if results:
                search_result_window = Toplevel(self.root)
                search_result_window.title("Search Results")

                listbox = tk.Listbox(search_result_window, width=50, height=10)
                listbox.pack(pady=10, padx=10)

                for contact in results:
                    listbox.insert(tk.END, contact['name'])
            else:
                messagebox.showinfo("Search Results", "No contacts found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a search query.")

    # Update the selected contact
    def update_contact(self):
        selected_contact_index = self.listbox.curselection()
        if selected_contact_index:
            contact = self.contacts[selected_contact_index[0]]
            self.contact_window = Toplevel(self.root)
            self.contact_window.title("Update Contact")

            Label(self.contact_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
            self.name_entry = Entry(self.contact_window)
            self.name_entry.insert(0, contact['name'])
            self.name_entry.grid(row=0, column=1, padx=10, pady=5)

            Label(self.contact_window, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
            self.phone_entry = Entry(self.contact_window)
            self.phone_entry.insert(0, contact['phone'])
            self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

            Label(self.contact_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
            self.email_entry = Entry(self.contact_window)
            self.email_entry.insert(0, contact['email'])
            self.email_entry.grid(row=2, column=1, padx=10, pady=5)

            Label(self.contact_window, text="Address:").grid(row=3, column=0, padx=10, pady=5)
            self.address_entry = Entry(self.contact_window)
            self.address_entry.insert(0, contact['address'])
            self.address_entry.grid(row=3, column=1, padx=10, pady=5)

            Button(self.contact_window, text="Update", command=lambda: self.save_updated_contact(selected_contact_index[0])).grid(row=4, column=0, columnspan=2, pady=10)
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    # Save the updated contact details
    def save_updated_contact(self, index):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone and email and address:
            self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            save_contacts(self.contacts)
            self.populate_listbox()
            self.contact_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please enter all details.")

    # Delete the selected contact
    def delete_contact(self):
        selected_contact_index = self.listbox.curselection()
        if selected_contact_index:
            del self.contacts[selected_contact_index[0]]
            save_contacts(self.contacts)
            self.populate_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
