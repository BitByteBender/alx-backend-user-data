#!/usr/bin/env python3
""" Password encryption using bcrypt """
import bcrypt


def hash_password(password: str) -> str:
    """ hash a password using bcrypt """
    gen_salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), gen_salt)
    return hashed
