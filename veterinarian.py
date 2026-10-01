class Veterinarian:
    def __init__(self, name):
        self.name = name

    def checkup(self, pet):
        print("Pet:", pet.name)
        print("Species:", pet.species)
        print("Health:", pet.health)

    def treat(self, pet, amount):
        pet.health = pet.health + amount
        print(pet.name, "was treated.")
        print("New health:", pet.health)