
from sqlalchemy import create_engine
from models.user import Base, User
from sqlalchemy.orm import sessionmaker, scoped_session
from models import DB_URI


class DBStorage:
    """Interface to the Database"""
    engine = None
    session = None

    def __init__(self) -> None:
        self.engine = create_engine(DB_URI, pool_pre_ping=True)

    def create_all(self):
        Base.metadata.create_all(self.engine)

    def drop_all(self):
        Base.metadata.drop_all(self.engine)

    def reload(self):
        self.create_all()
        session_factory = sessionmaker(
            bind=self.engine, expire_on_commit=False)
        self.session = scoped_session(session_factory)()

    def new(self, obj):
        self.session.add(obj)
        self.save()

    def save(self):
        self.session.commit()

    def delete(self, obj):
        self.session.expunge(obj)
        self.session.delete(obj)
        self.save()

    def all(self, cls=User):
        return self.session.query(cls).all()

    def close(self):
        self.session.close()

    def get(self, id, model=User):
        return self.session.get(model, id)
