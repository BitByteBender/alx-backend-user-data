#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            Method that adds a new user to the db
            Returns a newly created user obj
        """
        try:
            new_usr = User(email=email, hashed_password=hashed_password)
            self._session.add(new_usr)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_usr = None
        return new_usr

    def find_user_by(self, **kwargs) -> User:
        """ Method that finds a user by arbitrary keyword args """
        try:
            usr = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("User does not exist!")
        except InvalidRequestError:
            raise InvalidRequestError("Wrong query args are passed")
        return usr
