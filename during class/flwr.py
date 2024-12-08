class Flower:
    __slots__ = ['flower_name', 'botanical_id']

    def __init__(self, flower_name, botanical_id):
        self.flower_name = flower_name
        self.botanical_id = botanical_id

    def __hash__(self):
        return hash(self.botanical_id)
    
    def __eq__(self, other):
        if isinstance(other, Flower):
            return self.botanical_id == other.botanical_id
        return False
    
    def __str__(self):
        return f"Flower - {self.flower_name}, Botanical ID: {self.botanical_id}"
    

flower1 = Flower('Rose', 101)
flower2 = Flower('Lily', 102)
flower3 = Flower('Daisy', 103)

flower_dict = {
    flower1: "Perennial",
    flower2: "Annual",
    flower3: "Biennial"
}

duplicate_flower = Flower('Lily', 101)
flower_dict[duplicate_flower] = "Annual"

for flower, flower_type in flower_dict.items():
    print(f"{flower} - Type: {flower_type}")

print("\n Final Dictionary:")
for flower in flower_dict:
    print(flower)