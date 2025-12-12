import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_html(file_path):
    with open(file_path, "r") as handle:
        return handle


animals_data = load_data('animals_data.json')

output = ""

for animal in animals_data:
    output += f"""
    <li class="cards__item">
    Name: {animal['name']}<br/>
    Diet: {animal['characteristics']['diet']}<br/>
    Location: {", ".join(animal['locations'])}<br/>
    {('Type: ' + animal['characteristics']['type']) if animal['characteristics'].get('type') else ''}
    </li>
    """

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)
