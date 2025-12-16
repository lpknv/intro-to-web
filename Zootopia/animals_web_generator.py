import json


def get_animals_data():
    with open("animals_data.json", "r", encoding="utf-8") as file:
        return json.load(file)


def skin_types():
    types = []

    for animal in get_animals_data():
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type and skin_type not in types:
            types.append(skin_type)

    return types


def show_skin_types():
    for i, skin_type in enumerate(skin_types(), start=1):
        print(f"{i}. {skin_type}")


def animals_by_skin_type_serialized(skin_type):
    result = ""

    for animal in get_animals_data():
        animal_skin = animal.get("characteristics", {}).get("skin_type")
        if animal_skin and animal_skin.lower() == skin_type.lower():
            result += serialize_animal(animal)

    return result


def serialize_animal(animal):
    characteristics = animal["characteristics"]

    return f"""
        <li class="cards__item">
            <div class="card__title">{animal['name']}</div>
            <div class="card__text">
                <ul>
                    <li><strong>Diet:</strong> {characteristics['diet']}</li>
                    <li><strong>Skin Type:</strong> {characteristics['skin_type']}</li>
                    <li><strong>Location:</strong> {", ".join(animal['locations'])}</li>
                    <li><strong>Lifespan:</strong> {characteristics['lifespan']}</li>
                    {f"<li><strong>Type:</strong> {characteristics['type']}</li>" if characteristics.get("type") else ""}
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
    show_skin_types()

    skin_type_input = input("What skin type do you want to use? ").lower()

    if skin_type_input not in [t.lower() for t in skin_types()]:
        print("Skin type not found. Try again...")
        return

    output_animal_html_file(
        "animals_template.html",
        "animals.html",
        {
            "__REPLACE_SUBTITLE_FILTERED_BY_SKIN_TYPE__":
                f"<h2>Animals filtered by skin type: {skin_type_input}</h2>",
            "__REPLACE_ANIMALS_INFO__":
                animals_by_skin_type_serialized(skin_type_input)
        }
    )


if __name__ == "__main__":
    main()
