"""this module contains the FileStorage class

"""


import json


class FileStorage():
    """This class serializes instances to a json file and deserializes
    JSON file to instances

    Attributes:
        __file_path(string): path to json file
        __objects(dict): dictionary to store objects

    __init__: initializes all attributes

    """
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}
    def all(self):
        """this method returns dictionary containing objects

        Return:
            __objects(dict): dictionary containing objects

        """
        return (self.__objects)
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        """
        key = f"{obj['__class__']}.{obj['id']}"
        self.__objects[key] = obj
    def save(self):
        """serializes __objects to JSON file

        """
        with open(self.__file_path, 'w', encoding='utf-8') as fd:
            json.dump(self.__objects, fd)
    def reload(self):
        """deserializes the json file to __objects

        """
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                contents = (f.read()).rstrip()
                if contents:
                    self.__objects = json.loads(contents)
        except(FileNotFoundError):
            pass
