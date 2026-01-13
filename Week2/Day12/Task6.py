class Animal:
    species = 'Human'
    def __init__(self, name):
        self.name = name

animal1 = Animal("A")
print(f"species {animal1.species} name {animal1.name}")
Animal.species = "Dog"
print(f"species {animal1.species} name {animal1.name}")