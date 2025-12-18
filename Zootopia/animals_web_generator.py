import json


def get_animals_data():
    """Read animals.json using json library and return animals data"""
    with open("animals_data.json", "r", encoding="utf-8") as file:
        return json.load(file)


def skin_types(_animals):
    """Store skin types in new list from original animals list"""
    types = []

    for animal in _animals:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type and skin_type not in types:
            types.append(skin_type)

    return types


def show_skin_types(_animals):
    """Print available skin types"""
    for i, skin_type in enumerate(skin_types(_animals), start=1):
        print(f"{i}. {skin_type}")


def animals_by_skin_type_serialized(_animals, skin_type):
    """Filter animals by skin type and serialize them into an HTML string"""
    result = ""

    for animal in _animals:
        animal_skin = animal.get("characteristics", {}).get("skin_type")
        if animal_skin and animal_skin.lower() == skin_type.lower():
            result += serialize_animal(animal)

    return result


def add_card_text_item(title, characteristics, key):
    """Helper function to render a list item (HTML <li> tag)"""
    value = characteristics.get(key)
    if not value:
        return ""
    if isinstance(value, list):
        value = value[0]
    return f"<li><strong>{title}:</strong> {value}</li>"


def serialize_animal(animal):
    """Serialize an animal into an HTML string"""
    characteristics = animal["characteristics"]

    return f"""
        <li class="cards__item">
            <div class="card__title">{animal['name']}</div>
            <div class="card__text">
                <ul>
                    {add_card_text_item("Diet", characteristics, "diet")}
                    {add_card_text_item("Skin Type", characteristics, "skin_type")}
                    {add_card_text_item("Location", animal, "locations")}
                    {add_card_text_item("Lifespan", characteristics, "lifespan")}
                    {add_card_text_item("Type", characteristics, "type")}
                </ul>
            </div>
        </li>
    """


def output_animal_html_file(template_path, output_path, replacements):
    """
    1. Read the HTML template file
    2. Iterate through a dictionary to replace certain strings in the template file with the correct data
    3. Write the HTML output file
    """
    with open(template_path, "r", encoding="utf-8") as file:
        html = file.read()

    for key, value in replacements.items():
        html = html.replace(key, value)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html)


def main():
    """
    Load animal data from a JSON file, extract unique skin types,
    filter animals based on a user-provided skin type (case-insensitive),
    and generate an HTML file displaying the filtered results.
    """
    animals = get_animals_data()

    show_skin_types(animals)

    skin_type_input = input("What skin type do you want to use? ")

    if skin_type_input.lower() not in [t.lower() for t in skin_types(animals)]:
        print("Skin type not found. Try again...")
        return

    output_animal_html_file(
        "animals_template.html",
        "animals.html",
        {
            "__REPLACE_SUBTITLE_FILTERED_BY_SKIN_TYPE__":
                f"<h2>Animals filtered by skin type: {skin_type_input}</h2>",
            "__REPLACE_ANIMALS_INFO__":
                animals_by_skin_type_serialized(animals, skin_type_input)
        }
    )


if __name__ == "__main__":
    main()
