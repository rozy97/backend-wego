import json
from os import path

def create(user_data):
    basepath = path.dirname(__file__)
    filepath = path.join(basepath, "..", 'db/user.json')
    filename = path.abspath(filepath)

    with open(filename, "r+") as file:
        data = json.load(file)
        data.append(user_data)
        file.seek(0)
        json.dump(data, file)
        return user_data

def find():
    basepath = path.dirname(__file__)
    filepath = path.join(basepath, "..", 'db/user.json')
    filename = path.abspath(filepath)

    with open(filename, "r") as file:
        data = json.load(file)
        return data

def find_by_id(id):
    users = find()
    data = next((user for user in users if user["id"] == id), None)
    return data