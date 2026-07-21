import requests

API_KEY = "nRnJ3WGTEGolRVzQ2F7X2reLN9CYYD6BiWtyekEa"


def fetch_data(name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    """
        Function sends request (with API_KEY in header) to API with the variable "name". "Name" is the user input
        for the desired animal. It returns the json answer from the API or None if request is invalid.
    """
    
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return None