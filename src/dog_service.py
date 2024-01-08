class Dog():
    species = 'Range'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f'My dog Name is {self.name} and his age is {self.age} '