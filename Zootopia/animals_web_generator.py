import json


def get_animals_data():
    with open("animals_data.json", "r", encoding="utf-8") as file:
        return json.load(file)


def skin_types(_animals):
    types = []

    for animal in _animals:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type and skin_type not in types:
            types.append(skin_type)

    return types


def show_skin_types(_animals):
    for i, skin_type in enumerate(skin_types(_animals), start=1):
        print(f"{i}. {skin_type}")


def animals_by_skin_type_serialized(_animals, skin_type):
    result = ""

    for animal in _animals:
        animal_skin = animal.get("characteristics", {}).get("skin_type")
        if animal_skin and animal_skin.lower() == skin_type.lower():
            result += serialize_animal(animal)

    return result


def add_card_text_item(title, characteristics, key):
    value = characteristics.get(key)
    if not value:
        return ""
    if isinstance(value, list):
        value = value[0]
    return f"<li><strong>{title}:</strong> {value}</li>"


def serialize_animal(animal):
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
    with open(template_path, "r", encoding="utf-8") as file:
        html = file.read()

    for key, value in replacements.items():
        html = html.replace(key, value)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html)


def main():
    # get animals data from json file
    animals = get_animals_data()

    # show available skin types from all animals (without duplicates)
    show_skin_types(animals)

    # read the skin type from user input and transform it to lower case
    skin_type_input = input("What skin type do you want to use? ")

    # compare the user input to available skin types in lower case
    if skin_type_input.lower() not in [t.lower() for t in skin_types(animals)]:
        print("Skin type not found. Try again...")
        return

    # output html file with appropriate animals data
    output_animal_html_file(
        "animals_template.html",
        "animals.html",
        {
            # although not really necessary, indicate in the HTML that animals are filtered by skin type
            "__REPLACE_SUBTITLE_FILTERED_BY_SKIN_TYPE__":
                f"<h2>Animals filtered by skin type: {skin_type_input}</h2>",
            "__REPLACE_ANIMALS_INFO__":
                animals_by_skin_type_serialized(animals, skin_type_input)
        }
    )


if __name__ == "__main__":
    main()
