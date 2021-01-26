class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        pokenon_names = [p.name for p in self.pokemon]
        if pokemon_name not in pokenon_names:
            return f"Pokemon is not caught"
        del self.pokemon[pokemon_name.index(pokemon_name)]
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        trainer_info=[
            f"Pokemon Trainer {self.name}",
            f"Pokemon count {len(self.pokemon)}"
        ]
        pokemon_info = [f"- {p.pokemon_details ()}" for p in self.pokemon]
        return '\n'.join(trainer_info+pokemon_info) + '\n'
