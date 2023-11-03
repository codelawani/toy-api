from marshmallow import Schema, fields, validate
from sqlalchemy import Column, String, Integer, DateTime
from uuid import uuid4
from datetime import datetime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(String(60), default=uuid4, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    name = Column(String(50), nullable=False)
    age = Column(Integer)
    location = Column(String(60))
    email = Column(String(40), unique=True, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialise user model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S')
                if key != __class__:
                    setattr(self, key, val)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the object"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = value.strftime('%Y-%m-%dT%H:%M:%S')
        return dictionary

    def save(self, obj):
        from .engine import storage
        storage.save(obj)
        self.updated_at = datetime.now()


class UserSchema(Schema):
    email = fields.Email(required=True)
    name = fields.Str(validate=validate.Length(min=1))
    age = fields.Int()
    location = fields.Str(validate=validate.Length(min=1))
