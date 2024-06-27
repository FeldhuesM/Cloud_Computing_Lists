import json

def save_to_json(lists, filename='lists.json'):
    with open(filename, 'w') as file:
        json.dump(lists, file)