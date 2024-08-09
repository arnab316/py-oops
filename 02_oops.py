class Person:
    # ? initializing a constructor
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    def info(self):
        print(f"{self.name} is a a {self.occupation}")


a = Person("neha" , "hr" )
a.info()