#!/usr/bin/env python3
"""
Identity Service main logic
"""
from typing import Dict, Any
import json
import os

def conv_json_to_dict(data):
    """
    Convert json data to dict
    """
    if isinstance(data, str):
        return json.loads(data)

    if isinstance(data, dict):
        return data

    return dict()

class IdentityService():
    """
    Identity Service class with main logic
    """

    def __init__(self):
        self.data = dict()
        self.data["identities"] = []

    def register(self, username: str, password: str, properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registers an user with its username, password and properties
        """
        idt = {}

        try:
            idt = {
                "username": username,
                "password": password,
                "properties": conv_json_to_dict(properties)
            }

            self.data["identities"].append(idt)

        except ValueError as err:
            raise Exception("Couldn't load 'properties'. Is it a valid JSON?") from err

        return idt

    def authenticate(self, username: str, password: str) -> bool:
        """
        Authenticates an user using the provided username and password
        """
        for identity in self.data["identities"]:
            if identity["username"].casefold() == username.casefold() and \
               identity["password"] == password:
                return True
        return False

    def save_to_json(self, path: str, overwrite: bool = False):
        """
        Serializes this object to disk as a json text file
        """
        mode = "w" if overwrite else "x"

        try:
            with open(path, mode, encoding='utf-8') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False)

        except FileExistsError as err:
            raise Exception("File already exists and overwrite is not enforced") from err

        except IOError:
            print("File not accessible")

    def load_to_json(self, path: str):
        """
        Deserializes a json text file
        """
        # keep the dict empty
        if not os.path.isfile(path):
            return

        try:
            with open(path, "r") as json_file:
                data = json.load(json_file)

            self.data = data

        except ValueError as err:
            raise Exception("Couldn't load json from file") from err

        except IOError:
            print("File not accessible")
