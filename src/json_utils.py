import json

def get_json_file(path):
  with open(path, 'rb') as bills_file:
    return json.loads(bills_file.read())
