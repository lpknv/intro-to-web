import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_obj):
    """ Serializes an animal object """
    output = ""
    output += f"""
                <li class="cards__item">
                    <div class="card__title">{animal_obj['name']}</div>
                    <p class="card__text">
                        <strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>
                        <strong>Location:</strong> {", ".join(animal_obj['locations'])}<br/>
                        {('<strong>Type:</strong> ' + animal_obj['characteristics']['type']) if animal_obj['characteristics'].get('type') else ''}
                    </p>
                </li>
        """
    return output


animals_data = load_data('animals_data.json')

output = ""

for animal in animals_data:
    output += serialize_animal(animal)

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)
