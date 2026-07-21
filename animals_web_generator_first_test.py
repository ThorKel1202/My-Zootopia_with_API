import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
    
def give_info():
    animals_data = load_data("animals_data.json")
    for animal in animals_data:
        name_value = animal.get("name")
        if name_value:
            print(f"\nName: {name_value}")
            
        diet_value = animal.get("characteristics", {}).get("diet", "")
        if diet_value:
            print(f"Diet: {diet_value}")
            
        locations_value = animal.get("locations", [])
        if locations_value:
            print(f"Location: {locations_value[0]}")
            
        type_value = animal.get("characteristics", {}).get("type", "")
        if type_value:
            print(f"Type: {type_value}")

def main():
    # animals_data = load_data('animals_data.json')
    # print(animals_data)
    give_info()
    
if __name__ == "__main__":
    main()
