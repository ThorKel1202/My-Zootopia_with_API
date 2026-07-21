from flask import Flask, render_template, request
import json
import requests

API_KEY = "nRnJ3WGTEGolRVzQ2F7X2reLN9CYYD6BiWtyekEa"

app = Flask(__name__)


def get_animals(name):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return None


def serialize_animal(animal):
    single_animal_output = ''
    single_animal_output += '<li class="cards__item">\n'

    name_value = animal.get("name")
    if name_value:
        single_animal_output += f'<div class="card__title">{name_value}</div>\n'

    single_animal_output += '<div class="card__text">\n<ul>\n<p> </p>\n'

    scientific_name = animal.get("taxonomy", {}).get("scientific_name", "")
    if scientific_name:
        single_animal_output += f'<li><strong>Scientific name:</strong> {scientific_name}</li>\n'

    color = animal.get("characteristics", {}).get("color", "")
    if color:
        single_animal_output += f'<li><strong>Color:</strong> {color}</li>\n'

    diet = animal.get("characteristics", {}).get("diet", "")
    if diet:
        single_animal_output += f'<li><strong>Diet:</strong> {diet}</li>\n'

    locations = animal.get("locations", [])
    if locations:
        locations_str = ", ".join(locations)
        single_animal_output += f'<li><strong>Location:</strong> {locations_str}</li>\n'

    type_value = animal.get("characteristics", {}).get("type", "")
    if type_value:
        single_animal_output += f'<li><strong>Type:</strong> {type_value}</li>\n'

    single_animal_output += '</ul>\n</div>\n</li>\n'

    return single_animal_output


def make_string(user_animal_json):
    animals_data = json.loads(user_animal_json)
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


# 👉 ROUTE (Webseite)
@app.route("/", methods=["GET", "POST"])
def home():
    animals_html = ""

    if request.method == "POST":
        animal_name = request.form.get("animal")

        json_data = get_animals(animal_name)
        if json_data:
            animals_html = make_string(json_data)

    return render_template("index.html", animals=animals_html)


if __name__ == "__main__":
    app.run(debug=True)