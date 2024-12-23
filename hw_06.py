from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
     def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:     # Check for validity of input
            raise ValueError
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        p = self.find_phone(old_phone)
        if p:                                       #  if the old phone was found, remove it and add new phone
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
        else:
            raise ValueError                        #  if the old phone wasn't found
            
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]  

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p                                # Return the matching Phone object
        return None                                     # Return None if phone is not found

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    def add_record(self, record):                   # Add a Record item to the address book
        self.data[record.name.value] = record

    def find(self, name):                    # Find and return a Record item by name
        return self.data.get(name) 

    def delete(self, name):                     # Delete a Record item by name
        if name in self.data:
            del self.data[name]
       

    def __str__(self):
        return "\n".join([str(record) for record in self.data.values()]) #output of records

