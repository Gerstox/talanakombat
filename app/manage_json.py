import json

class ManageJson:
  def read_json(self, filename):
    fights_file = open(filename)
    fights = json.load(fights_file)
    return fights
