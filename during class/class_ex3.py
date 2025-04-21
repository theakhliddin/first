class Pet:
    __slots__ = ['species', 'name', 'weight', 'fur_color', 'age']
    
    def __init__(self, species, name, weight, fur_color, age=0):
        self.species = species
        self.name = name
        self.weight = weight
        self.fur_color = fur_color
        self.age = age

def main():
    my_pet = Pet('dog', 'Buddy', 25.5, 'brown')
    print("Name", my_pet.name)
    print("Species", my_pet.species)
if __name__ == "__main__":
    main()