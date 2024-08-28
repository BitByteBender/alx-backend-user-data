#!/usr/bin/env python3
""" Tasks -> Regex-ing """
import logging
import re
from typing import List


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "*"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init the RedactingFormatter with the given fields """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record to redact sensitive data """
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
