from sqlalchemy import Column, String, Integer, DateTime
from uuid import uuid4
from datetime import datetime


class User:

    id = Column(String(60), default=uuid4, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    name = Column(String(50))
    age = Column(Integer)
    location = Column(String(60))
