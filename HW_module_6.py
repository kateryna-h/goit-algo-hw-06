from collections import UserDict
import HW_5

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
     def __init__(self, phone):
        if len(phone) < 10:
            super().__init__("Phone is too short")   
        elif len(phone) > 10:
            super().__init__("Phone is too long")  

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone: str):
        phone_number = self.find_phone(phone)
        self.phones.remove(phone_number)
        
    def edit_phone(self, old_phone, new_phone):
        phone_number = self.find_phone(old_phone)
        if phone_number:
            phone_number.value = new_phone
            raise ValueError
    
    def find_phone(self, phone: str):
         for i in self.phones:
              if i.value == phone:
                   return i
              return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name: str):
           return self.data.get(name)
        
    def delete(self, name):
           return self.data.pop(name, None)
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
        
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі 
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
