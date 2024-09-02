#!/usr/bin/env python3
""" Authentication module """
from flask import request
from fnmatch
from typing import List, TypeVar


class Auth:
    """ Auth-sys Template """
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """
        Check if auth is required
        Returns True if auth is required otherwise False
        """
        if not path or not excluded_paths:
            return True

        for ep in excluded_paths:
            if fnmatch.fnmatchcase(path, ep):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the auth header from the request
        Returns None
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets current user from request
        Returns None
        """
        return None
