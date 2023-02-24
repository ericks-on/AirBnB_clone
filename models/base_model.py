"""this module contains the base module class
"""


import uuid
import datetime
from dateutil import parser
from models import storage

class BaseModel():
    """this is the base model class 

    Attributes:
        id(string): an uuid assigned when instance is created
        created_at(datetime): current datetime when an instance is created
        updated_at(datetime): current datetime when an instance is created
                                and it will be updated every time you 
                                change your object

    __init__: initializes the class attributes

    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs.keys():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        date = parser.parse(kwargs[key])
                        setattr(self, key, date)
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at  = datetime.datetime.now()
            self.updated_at = self.created_at
        if args:
            for obj in args:
                storage.new(obj)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime

        """
        updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        the_dict = self.__dict__
        the_dict['__class__'] = self.__class__.__name__
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()
        return (the_dict)
