#!/usr/bin/env python3
""" Authentication module """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth-sys Template """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if auth is required
        Returns a boolean
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Gets the auth header from the request
        Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets current user from request
        Returns None
        """
