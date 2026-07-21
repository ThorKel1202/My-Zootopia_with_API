import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

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
        single_animal_output += f'    <div class="card__title">{name_value}</div>\n'
    
    single_animal_output += '    <div class="card__text">\n'
    single_animal_output += '       <ul>\n'
    single_animal_output += '          <p> </p>\n'
    
    scientific_name_value = animal.get("taxonomy", {}).get("scientific_name", "")
    if scientific_name_value:
        single_animal_output += f'          <li class="single_info_text_row"><strong>Scientific name:</strong> {scientific_name_value}</li>\n'
        
    color_value = animal.get("characteristics", {}).get("color", "")
    if color_value:
        single_animal_output += f'          <li class="single_info_text_row"><strong>Color:</strong> {color_value}</li>\n'
        
    diet_value = animal.get("characteristics", {}).get("diet", "")
    if diet_value:
        single_animal_output += f'          <li class="single_info_text_row"><strong>Diet:</strong> {diet_value}</li>\n'
    
    locations_value = animal.get("locations", [])
    if locations_value:
        if len(locations_value) == 1:
            locations_str = locations_value[0]
        else:
            locations_str = ", ".join(locations_value[:-1]) + " and " + locations_value[-1]
        
        single_animal_output += f'          <li class="single_info_text_row"><strong>Location:</strong> {locations_str}</li>\n'
    
    type_value = animal.get("characteristics", {}).get("type", "")
    if type_value:
        single_animal_output += f'          <li class="single_info_text_row"><strong>Type:</strong> {type_value}</li>\n'
    
    single_animal_output += '       </ul>\n'
    
    single_animal_output += '   </div>\n'
    
    single_animal_output += '</li>\n'


    return single_animal_output
    
    

def make_string():
    """
        The function first put all the JSON data into "animals_data. Then it creates a string, called
        "output". Then it iterates through all the animal data in the JSON file and sends each single
        one to "serialize_animal". After the return, it appends all to "output" and creates a complete
        string which can be copied directly into the html template for usage there. Finally, it returns
        the complete "output" string to the main function to print it.
    """
    
    animals_data = load_data("animals_data.json")
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
        
    return output
        
    
def main():
    print(make_string())
    
if __name__ == "__main__":
    main()

