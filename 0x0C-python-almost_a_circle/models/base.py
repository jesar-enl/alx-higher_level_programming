#!/usr/bin/python3
"""Module to contain the ``Base`` class"""
import json
import os.path
import csv


class Base:
    """Class definition of ``Base``"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the constructor of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """return the actual object representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of objects to files"""
        if list_objs is None:
            objs = "[]"
        else:
            obj_dict = []
            for obj in list_objs:
                obj_dic = obj.to_dictionary()
                obj_dict.append(obj_dic)
            objs = Base.to_json_string(obj_dict)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(objs)

    @classmethod
    def create(cls, **dictionary):
        """Create a new object from the values in dictionary"""
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Create a new instance from the contents of the file"""
        filename = "{}.json".format(cls.__name__)
        list_objs = []
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as fp:
                json_string = fp.read()
            list_dictionaries = Base.from_json_string(json_string)
            for dictionary in list_dictionaries:
                obj = cls.create(**dictionary)
                list_objs.append(obj)
            return list_objs
