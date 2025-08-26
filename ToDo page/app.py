from flask import Flask, render_template, request, redirect
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client.todo_db
collection = db.todo_items

@app.route('/')
def index():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['GET', 'POST'])
def submit():
    # data = request.get_json()
    data = request.form.to_dict()
    print(data)
    collection.insert_one(data)
    return "Item added successfully"


if __name__ == '__main__':  
    app.run(debug=True)
