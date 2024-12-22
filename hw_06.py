from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
     def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError("Phone number must be a 10-digit format.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                try:                                    
                    self.phones[i] = Phone(new_phone) 
                    return True
                except ValueError:
                        print(f"Phone number must be a 10-digit format.")
                        return False
        return False                                    #  if old_phone is not found

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def find_phone(self, phone):
        return any(p.value == phone for p in self.phones)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):                   # Add a Record item to the address book
        self.data[record.name.value] = record

    def find_record(self, name):                    # Find and return a Record item by name
        return self.data.get(name) 

    def delete_record(self, name):                     # Delete a Record item by name
        if name in self.data:
            del self.data[name]
            return True
        return False

    def __str__(self):
        return "\n".join([str(record) for record in self.data.values()]) #output of records

