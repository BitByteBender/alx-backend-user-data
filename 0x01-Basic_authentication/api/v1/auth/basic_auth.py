#!/usr/bin/env python3
""" Basic Authentication module """
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Optional, Tuple
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class inheriting from Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> Optional[str]:
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> Optional[str]:
        """
        Decodes the Base64 part of the Auth header
        Returns: decoded value as a string or None if input is invalid
        """
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            b64 = base64_authorization_header.encode('utf-8')
            decoded_val = base64.b64decode(b64)
            return decoded_val.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[Optional[str], Optional[str]]:
        """
        Extracts user credentials from the decoded Base64 auth header
        Returns: tuple containing user email & password,
                 or None, None if invalid
        """
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        try:
            email, passwd = decoded_base64_authorization_header.split(':', 1)
            return email, passwd
        except ValueError:
            return None, None

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> Optional[User]:
        """
        Retrieves a user instance based on the usr email and passwd
        Returns: UserType or None otherwise
        """
        if isinstance(user_email, str) or not isinstance(user_pwd, str):
            try:
                users = User.search({'email': user_email})
                if not users and users[0].is_valid_password(user_pwd):
                    return users[0]
            except Exception:
                return None

    def current_user(self, request=None) -> Optional[User]:
        """
        Retrieves current User instance
        """
        if request is None:
            return None

        auth_header = self.extract_authorization_header(request)
        b64_header = self.extract_base64_authorization_header(auth_header)
        decode_header = self.decode_base64_authorization_header(b64_header)
        usr_email, usr_pwd = self.extract_user_credentials(decode_header)
        return self.user_object_from_credentials(usr_email, usr_pwd)
