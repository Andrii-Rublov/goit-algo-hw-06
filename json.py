import json

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False
    },
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True
    }
]

def write_contacts_to_file(filename, contacts):
    contacts = {"contacts": contacts}
    with open(filename, "w") as fh:
        return json.dump(contacts, fh, indent=4)
    
        


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        return json.load(fh)
    
write_contacts_to_file("contacts.json", contacts)