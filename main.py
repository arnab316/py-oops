class Person :
    name = "Arnab"
    occupation = "Software Engineer"
    networth = "$10M"
    def info(self):
        print(f"{self.name} is a  {self.occupation}")
a = Person()
a.info()