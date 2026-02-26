#!/usr/bin/env python3
"""Returns the log message obfuscated"""
import logging
import re
from os import environ
from typing import List

import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns the log message obfuscated"""
    parts = message.split(separator)
    for idx, text in enumerate(parts):
        if text.startswith(tuple(fields)):
            parts[idx] = re.sub(r"(=)(.*)", rf"\1{redaction}", text)
    return separator.join(parts)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records using filter_datum"""
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """Returns a logging.Logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connection to the database"""
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password_db = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host_db = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    database_name = environ.get("PERSONAL_DATA_DB_NAME")
    conn = mysql.connector.connect(
        user=username,
        password=password_db,
        host=host_db,
        database=database_name
    )
    return conn
