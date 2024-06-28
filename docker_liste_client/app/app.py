from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)



@app.route('/')
def home():
    selected_list = request.args.get('list', 'Einkaufszettel')
    response = requests.get(f"http://192.168.178.94:5001/lists/{selected_list}")
    data = response.json()
    return render_template("index.html", lists=data['lists'], current_list=data['current_list'], list_name=selected_list)

@app.route('/add', methods=['POST'])
def add_item():
    list_name = request.form['list_name']
    item = request.form['item']
    response = requests.post("http://192.168.178.94:5001/add_item", json={'list_name': list_name, 'item': item})
    return redirect(url_for('home', list=list_name))


@app.route('/delete_item', methods=['POST'])
def delete_item():
    list_name = request.form['list_name']
    item = request.form['item_index']
    response = requests.post("http://192.168.178.94:5001/delete_item", json={'list_name': list_name, 'item': item})
    return redirect(url_for('home', list=list_name))

@app.route('/add_list', methods=['POST'])
def add_list():
    list_name = request.form['list_name']
    new_list_name = request.form['new_list']
    response = requests.post("http://192.168.178.94:5001/add_list", json={'list_name': list_name, 'new_list_name': new_list_name})
    return redirect(url_for('home', list=new_list_name))

@app.route('/delete_list', methods=['POST'])
def delete_list():
    list_name = request.form['list_name']
    response = requests.post("http://192.168.178.94:5001/delete_list", json={'list_name': list_name})
    return redirect(url_for('home', list='Einkaufszettel'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)






  
