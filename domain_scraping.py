import requests
import json

sample_values = []
url = "https://api.thedogapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=DESC&page=0&limit=10"


def Json_dump(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


def Separate_names_from_json(obj):
    return obj[0]["breeds"][0]["name"]


def Remember_old_values(obj):
    x = sample_values.append(obj)
    return x


def Get_json(url=url):
    response = requests.get(url)
    storage = response.json()
    remember_value = Separate_names_from_json(storage)
    Remember_old_values(remember_value)
    return remember_value
