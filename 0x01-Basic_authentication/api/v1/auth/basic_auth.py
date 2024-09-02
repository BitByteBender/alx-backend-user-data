#!/usr/bin/env python3
""" Basic Authentication module """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class inheriting from Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for basic_auth
        Returns: Base64 or None if header is invalid
        """
        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return (authorization_header.split("Basic ")[1]
                if "Basic " in authorization_header else None)
