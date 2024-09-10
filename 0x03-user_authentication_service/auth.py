#!/usr/bin/env python3
""" Auth: Password hasher """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Password hashing using bcrypt """
    hashed_pwd = bcrypt.hashpw(password.encode("utf-8"),
                               bcrypt.gensalt())
    return hashed_pwd
