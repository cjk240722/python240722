class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# Test 1: Create a Person object and print info
p1 = Person(1, "Alice")
p1.printInfo()
# Expected Output:
# ID: 1, Name: Alice

# Test 2: Create a Manager object and print info
m1 = Manager(2, "Bob", "Project Manager")
m1.printInfo()
# Expected Output:
# ID: 2, Name: Bob
# Title: Project Manager

# Test 3: Create an Employee object and print info
e1 = Employee(3, "Charlie", "Python Developer")
e1.printInfo()
# Expected Output:
# ID: 3, Name: Charlie
# Skill: Python Developer

# Test 4: Create another Person object and print info
p2 = Person(4, "David")
p2.printInfo()
# Expected Output:
# ID: 4, Name: David

# Test 5: Create another Manager object with different title and print info
m2 = Manager(5, "Eve", "Team Lead")
m2.printInfo()
# Expected Output:
# ID: 5, Name: Eve
# Title: Team Lead

# Test 6: Create another Employee object with different skill and print info
e2 = Employee(6, "Frank", "Data Scientist")
e2.printInfo()
# Expected Output:
# ID: 6, Name: Frank
# Skill: Data Scientist

# Test 7: Test the inheritance by checking if Manager is instance of Person
print(isinstance(m1, Person))
# Expected Output:
# True

# Test 8: Test the inheritance by checking if Employee is instance of Person
print(isinstance(e1, Person))
# Expected Output:
# True

# Test 9: Test the inheritance by checking if Manager is not instance of Employee
print(isinstance(m1, Employee))
# Expected Output:
# False

# Test 10: Test the inheritance by checking if Employee is not instance of Manager
print(isinstance(e1, Manager))
# Expected Output:
# False
