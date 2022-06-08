import os
import json

def list_dir(path):
    return os.listdir(path)

def read_json(file_name):
    if file_name.endswith(".json") == False: return False
    f = open(file_name)
    data = json.load(f)
    f.close()
    return data

def try_write_array(data, output_path, file_name):
    if len(data) == 0: return False
    path = os.path.join(output_path, file_name)
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
    return True