from os import path

basepath = path.dirname(__file__)
filepath = path.join(basepath, "..", 'db/last_id.txt')
filename = path.abspath(filepath)

def generate_id():
    with open(filename, 'r') as file:
        file_data = file.read()
        file.close()
        last_id = int(file_data)
        update_last_id(last_id + 1)
        return last_id + 1

def update_last_id(last_id):
    with open(filename, 'w') as file:
        file_data = str(last_id)
        file.write(file_data)
        file.close()
        return True
