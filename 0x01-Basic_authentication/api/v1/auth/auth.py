#!/usr/bin/env python3
"""
3. Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ a class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for the given path."""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            excluded_paths = [excluded_path.rstrip('/')]
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Extracts the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user from the request."""
        return None
