from flask import Flask, request, redirect, jsonify, url_for
from load_from_json import load_from_json
from save_to_json import save_to_json
app = Flask(__name__)

lists = {}

@app.route('/lists/<list_name>')
def get_list(list_name):
    return jsonify({'lists': lists, 'current_list': lists.get(list_name, []), 'list_name': list_name})

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    lists[data['list_name']].append(data['item'])
    save_to_json(lists)  # Angenommen, diese Funktion existiert bereits
    return jsonify(success=True)

@app.route('/delete_item', methods=['POST'])
def delete_item():
    data = request.get_json()
    list_name = data['list_name']
    item_index = int(data['item'])

    if 0 <= item_index < len(lists[list_name]):
        if item_index == 'Einaufszettel':
            return redirect(url_for('home', list=list_name))
        lists[list_name].pop(item_index)
        save_to_json(lists)
 
    return jsonify(success=True)

@app.route('/add_list', methods=['POST'])
def add_list():
    data = request.get_json()
    if data['new_list_name'] not in lists:
        lists[data['new_list_name']] = []
        save_to_json(lists)  
    return jsonify(success=True)

@app.route('/delete_list', methods=['POST'])
def delete_list():
    data = request.get_json()
    del lists[data['list_name']]
    save_to_json(lists)  
    return jsonify(success=True)

# Ähnliche Endpunkte für delete_item, add_list, delete_list

if __name__ == '__main__':
    lists = load_from_json()  # Laden der Listen beim Start
    app.run(host='0.0.0.0', port=5001, debug=True)




