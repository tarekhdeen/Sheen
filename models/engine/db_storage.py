#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import Config
from models.base_model import BaseModel, Base
from models.appointment import Appointment
from models.clinic import Clinic
from models.doctor import Doctor
from models.patient import Patient
from models.procedure import Procedure
from models.user import User

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://sheen_user:Ta%40wa2892003@localhost/sheen_db')
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Query all objects"""
        session = self.__session()
        if cls:
            objects = session.query(cls).all()
        else:
            objects = session.query(BaseModel).all()
        return {obj.id: obj for obj in objects}

    def new(self, obj):
        """Add new object to session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in database and create a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
