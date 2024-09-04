#!/usr/bin/env python3
""" Session Auth mechanism """
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ SessionAuth class inherits from Auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method that creates a session_id for a user
        """
        if type(user_id) is not str or user_id is None:
            return None
        else:
            sess_id = str(uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id
