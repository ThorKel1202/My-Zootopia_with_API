from flask import Flask, render_template, request
import json
import data_fetcher

app = Flask(__name__)


def serialize_animal(animal):
    """
       Serializes an animal into a string by getting the wanted information. here it is
       the name of the animal, the FIRST location and out of its characteristics the diet
       and the type. Each one is checked, if there is the asked data or not. Along with the
       needed html-tags it becomes a complete html string for one animal out of the JSON file,
       which will be returned as single_animal_output.
    """
    
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
    """
        The function first put all the JSON data into "animals_data. Then it creates a string, called
        "output". Then it iterates through all the animal data in the JSON file and sends each single
        one to "serialize_animal". After the return, it appends all to "output" and creates a complete
        string which can be copied directly into the html template for usage there. Finally, it returns
        the complete "output" string to the main function to print it.
    """
    
    animals_data = json.loads(user_animal_json)
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


@app.route("/", methods=["GET", "POST"])
def home():
    animals_html = ""
    error_message = ""
    
    if request.method == "POST":
        animal_name = request.form.get("animal")
        json_data = data_fetcher.fetch_data(animal_name)
        if json_data:
            animals_data = json.loads(json_data)
            # Prüfung, ob Animal existiert!
            if len(animals_data) == 0:
                error_message = f"Sorry, the animal „{animal_name}“ does not exist."
            else:
                animals_html = make_string(json_data)
        else:
            error_message = "API error. Please try again."
    
    return render_template(
        "animals_with_api.html",
        animals=animals_html,
        error=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)