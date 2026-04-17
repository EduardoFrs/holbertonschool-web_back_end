#!/usr/bin/env python3
"""Basic auth"""

from typing import TypeVar
import base64
import binascii
import re
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        """Return the Base64 part of the Authorization
            header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return
        value = re.search(r"[^\s]*$", authorization_header)
        return value.group()

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Return the decoded value of a Base64
           string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            valid = base64.b64decode(
                base64_authorization_header, validate=True
                )
            if valid:
                return valid.decode("utf-8")
        except binascii.Error:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Return the user email and password
           from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" in decoded_base64_authorization_header:
            res = decoded_base64_authorization_header.split(":")
            return tuple(res)
        else:
            return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Return the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance for a request"""
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
                auth_header)
        if not base64_auth_header:
            return None

        decode_auth_header = self.decode_base64_authorization_header(
                base64_auth_header)
        if not decode_auth_header:
            return None

        user_email, user_pwd = self.extract_user_credentials(
                decode_auth_header)
        if not user_email or not user_pwd:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
