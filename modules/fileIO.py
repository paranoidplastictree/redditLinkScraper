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

def read_json_lines(file_name):
    if file_name.endswith(".jsonl") == False: return False
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(json.loads(line))
        f.close()
    return data

def try_write_array(data, output_path, file_name):
    if len(data) == 0: return False
    path = os.path.join(output_path, file_name)
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
    return True

def write_dict(dictionary, output_path, file_name):
    path = os.path.join(output_path, file_name)
    dict_json = json.dumps(dictionary)
    with open(path, 'a') as outfile:
        outfile.write("{}\n".format(dict_json))
