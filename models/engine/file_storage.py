#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    # All
    # Updated to return the list of objects of one type of class
    # ============================================================ #

    def all(self, cls=None):
        """Returns a dict or filtered list of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            return {key: obj for key, obj in FileStorage.__objects.items()
                    if isinstance(obj, cls)}

    # New
    # ============================================================ #

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    # Save
    # ============================================================ #

    def save(self):
        """ Saves storage dictionary to file """
        with open(FileStorage.__file_path, 'w') as f:

            temp = {
                key: val.to_dict() for key,
                val in FileStorage.__objects.items()
            }

            json.dump(temp, f, indent=4)

    # Reload
    # ============================================================ #

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    # Delete
    # ============================================================ #

    def delete(self, obj=None):
        """ Deletes an object from the storage dict """
        if obj is None:
            return
        else:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    # Close
    # ============================================================ #
    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()
