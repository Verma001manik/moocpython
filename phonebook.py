class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
    
    def get_name(self, number):
        for name,numbers in self.__persons.items():
            if number in numbers:
                return name
        return None
    def ad_address(self,name,address):
        if not name in self.__persons:
            self.__persons[name]  = Person(name)
        self.__persons[name].add_address(address)

    
    

    def all_entries(self):
        return self.__persons
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 addentry")
        print("2 search")
        print("3 search with number")
        print("4 add address")
    
    def add_add(self):
        name = input("name")
        address  = input("address")
        self.__phonebook.ad_address(address=address)

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        
        self.__phonebook.add_number(name,number)

    def search(self):
        name = input("name:")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return 
        for number in numbers:
            print(number)

    def search_with_number(self):
        number = input("number:")
        name = self.__phonebook.get_name(number)
        if name == None:
            print("Number Unknown")
        else:
            print(name)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command =="1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_with_number()
            elif command =="4":
                self.add_add()
            else:
                self.help()
                

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                
                name, *numbers = parts
                
                names[name] = numbers

        return names
    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")



class Person:
    def __init__(self, name):
        self.person_name = name 
        self.person_number = []
        self.person_address = ""
    def name(self):
        return self.person_name
    def numbers(self):
        return self.person_number
    def address(self):
        if self.person_address == "":
            return None
        else:
            return self.person_address
    def add_number(self,number):
        if number not in self.person_number:
            self.person_number.append(number)

    def add_address(self,address):
        if address not in self.person_address:
            self.person_address  = address
    
    def __str__(self):
        return f"{self.person_address}\n {self.person_number}\n {self.person_address}"
application = PhoneBookApplication()
application.execute()