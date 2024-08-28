#!/usr/bin/env python3
""" Task 0 -> Regex-ing """
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
