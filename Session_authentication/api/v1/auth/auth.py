#!/usr/bin/env python3
"""Auth class"""


from typing import List, TypeVar

from flask import request


class Auth:
    """Basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Define which routes don't need authentication"""
        if path is None:
            return True
        if excluded_paths == [] or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False

        if (
            path == "/api/v1/status" or path == "/api/v1/status/"
        ) and "/api/v1/status/" in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Request validation"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """Public method that return None"""
        if request is None:
            return None
