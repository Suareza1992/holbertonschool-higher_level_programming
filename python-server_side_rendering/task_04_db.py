from flask import Flask, render_template, request
import json
import csv
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def read_json_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def read_csv_data(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def read_database():
    pass

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        try:
            products = read_json_data('products.json')
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found.")
    elif source == 'csv':
        try:
            products = read_csv_data('products.csv')
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found.")
    else:
        return render_template('product_display.html', error="Wrong source.")


    if id:
        filtered_products = [product for product in products if str(product['id']) == id]
        if not filtered_products:
            return render_template('product_display.html', error=f"Product with ID {id} not found.")
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
