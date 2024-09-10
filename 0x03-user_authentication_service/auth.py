#!/usr/bin/env python3
""" Auth: Password hasher """
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Password hashing using bcrypt """
    hashed_pwd = bcrypt.hashpw(password.encode("utf-8"),
                               bcrypt.gensalt())
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Inits newly created Auth instance """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Inserts the newly created user into the database """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate the user loging infos
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(password.encode("utf-8"),
                                      user.hashed_password)
        except NoResultFound:
            return False
        return False
