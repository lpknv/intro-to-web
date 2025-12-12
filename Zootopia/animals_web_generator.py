import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


for animal in animals_data:
    print(f"""
    Name: {animal['name']}
    Diet: {animal['characteristics']['diet']}
    Location: {", ".join(animal['locations'])}
    {('Type: ' + animal['characteristics']['type']) if animal['characteristics'].get('type') else ''}
    """)