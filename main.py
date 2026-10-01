from pet import Pet
from veterinarian import Veterinarian

vet = Veterinarian("Dr. Smith")

pet1 = Pet("Buddy", "Dog", 60)
pet2 = Pet("Milo", "Cat", 75)
pet3 = Pet("Coco", "Rabbit", 50)

print("PET 1")
vet.checkup(pet1)

print("\nTreating Buddy")
vet.treat(pet1, 20)

print("\nBuddy after treatment")
vet.checkup(pet1)

print("\nPET 2")
vet.checkup(pet2)

print("\nTreating Milo")
vet.treat(pet2, 15)

print("\nMilo after treatment")
vet.checkup(pet2)

print("\nPET 3")
vet.checkup(pet3)

print("\nTreating Coco")
vet.treat(pet3, 25)

print("\nCoco after treatment")
