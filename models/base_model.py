#!/usr/bin/python3
""" This file is for the baseModel for the airbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ this is the contructor of the baseModel class
        """
        self.id = uuid.uuid4().__str__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    def save(self):
        """ this is the method to save the class
        """
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """ this is the first function for the serialization
        """
        mydict = {}
        for key, value in self.__dict__.items():
            if type(value) == datetime:
                mydict[key] = value.isoformat()
            else:
                mydict[key] = value
        mydict["__class__"] = self.__class__.__name__
        return mydict
