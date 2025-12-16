import json


def skin_types():
    types = []

    for animal in get_animals_data():
        characteristics = animal.get("characteristics")
        if not characteristics:
            continue

        skin_type = characteristics.get("skin_type")
        if not skin_type:
            continue

        if skin_type not in types:
            types.append(skin_type)

    return types


def show_skin_types():
    counter = 0
    for skin_type in skin_types():
        counter += 1
        print(f"{counter}. {skin_type}")


def animals_by_skin_type_serialized(skin_type):
    result = ""

    for animal in get_animals_data():
        if animal["characteristics"].get("skin_type") == skin_type:
            result += serialize_animal(animal)

    return result


def read_file(file_path, file_type):
    with open(file_path, "r", encoding="utf-8") as handle:
        if file_type == "json":
            return json.load(handle)
        else:
            return handle.read()


def write_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)


def serialize_animal(animal_obj):
    html_output = ""
    html_output += f"""
                <li class="cards__item">
                    <div class="card__title">{animal_obj['name']}</div>
                    <div class="card__text">
                        <ul>
                            <li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>
                            <li><strong>Skin Type:</strong> {animal_obj['characteristics']['skin_type']}</li>
                            <li><strong>Location:</strong> {", ".join(animal_obj['locations'])}</li>
                            <li><strong>Lifespan:</strong> {animal_obj['characteristics']['lifespan']}</li>
                            {('<li><strong>Type:</strong> ' + animal_obj['characteristics']['type'] + '</li>') if animal_obj['characteristics'].get('type') else ''}
                        </ul>
                    </div>
                </li>
        """
    return html_output


def get_animals_data():
    return read_file("animals_data.json", 'json')


def output_animal_html_file(file_template, output_path, data_to_replace):
    html_content = read_file(file_template, None)
    for key, val in data_to_replace.items():
        html_content = html_content.replace(key, val)
    write_file(output_path, html_content)


def main():
    show_skin_types()

    skin_type = input("What skin type do you want to use? ").lower()

    available_skin_types = []
    for t in skin_types():
        available_skin_types.append(t.lower())

    if skin_type not in available_skin_types:
        print("Skin type not found. Try again...")
        return

    output_animal_html_file(
        "animals_template.html",
        f"animals_filtered_by_skin_type_{skin_type}.html",
        {
            "__REPLACE_SUBTITLE_FILTERED_BY_SKIN_TYPE__": f"<h2>Animals filtered by skin type: {skin_type}</h2>",
            "__REPLACE_ANIMALS_INFO__": animals_by_skin_type_serialized(
                skin_type
            )
        }
    )


if __name__ == "__main__":
    main()
