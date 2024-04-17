#!/usr/bin/env python3
"""
3. Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for the given path."""
        return False


    def authorization_header(self, request=None) -> str:
         """Extracts the authorization header from the request."""
         return  None


    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user from the request."""
        return None
