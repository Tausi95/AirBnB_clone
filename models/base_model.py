# models/base_model.py

#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime

class BaseModel:
    """Represents the base model for all classes."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
    
    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
    
    def __str__(self):
        """Return the string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

