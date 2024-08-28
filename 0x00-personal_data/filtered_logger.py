#!/usr/bin/env python3
""" Tasks -> Regex-ing """
import logging
import re
from typing import List, Tuple


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Returns the log msg obfuscated by replacing field vals """
    ptrn = r"({})=[^{}]*".format('|'.join(fields), separator)
    return re.sub(ptrn, lambda match: "{}={}".format(
                  match.group(1),
                  redaction),
                  message)


PII_FIELDS: Tuple[str, str, str, str, str] = ("name", "email", "phone",
                                              "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init the RedactingFormatter with the given fields """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record to redact sensitive data """
        msg = super().format(record)
        output = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return output


def get_logger() -> logging.Logger:
    """ Creates and returns a logger configuree with RedactingFormatter """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
