import json


def main():
    # TODO: build a list of 3 animal dictionaries
    animals = [
    {"name": "Rex", "age": 4, "species": "Dog", "breed": "Labrador"},
    {"name": "Mala", "age": 10, "species": "Cat", "indoor": True},
    {"name": "Tweety", "age": 2, "species": "Bird"},
]

    # TODO: write `animals` to "animals.json" using json.dump
    #   pattern:
    #   with open("animals.json", "w") as f:
    #       json.dump(..., f)
    with open("animals.json", "w") as f:
        json.dump(animals, f, indent=2)

    # TODO: read it back from "animals.json" using json.load
    #   pattern:
    #   with open("animals.json", "r") as f:
    #       loaded = json.load(f)
    with open("animals.json", "r") as f:
        loaded = json.load(f)

    # TODO: loop over `loaded` and print each animal's name and age
    for animal in loaded:
        print(f"{animal["name"]} is {animal["age"]} years old")


if __name__ == "__main__":
    main()