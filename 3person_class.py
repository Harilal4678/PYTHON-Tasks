class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_details(self):
        print(f"Person Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

person1 = Person("HARI", 24, "perinthalmanna")
person1.display_details()

