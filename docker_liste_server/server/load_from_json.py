import json

def load_from_json(filename='lists.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            'Einkaufszettel': [],
            'Aufgaben': [],
            'Wunschliste': []
        }