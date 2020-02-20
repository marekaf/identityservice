#!/usr/bin/env python3
import unittest
import os

from identityservice import identity_service as ids

class TestIdentityService(unittest.TestCase):

    def setUp(self):
        self.is1 = ids.IdentityService()

    def tearDown(self):
        del self.is1
        if os.path.isfile("users.json"): os.remove("users.json")

    def test_register(self):

        john = { "username": "john", "password": "12345", "properties": { "greeting": "Ahoj, John", "year_born": 1985, "hobbies": ["cars", "music", "python" ]  }}
        reg1 = self.is1.register(john["username"],john["password"],john["properties"])

        mark = { "username": "mark", "password": "12345", "properties": { "greeting": "Ahoj, Mark", "year_born": 1995, "hobbies": ["bike", "programming", "star wars" ] }}
        reg2 = self.is1.register(mark["username"],mark["password"],mark["properties"])

        jack = { "username": "jack", "password": "54321", "properties": { "greeting": "Hello, Jack", "year_born": 1987, "hobbies": ["cars", "tea", "ruby" ] }}
        reg3 = self.is1.register(jack["username"],jack["password"],jack["properties"])

        # let's add some diversity, shall we?
        ale = { "username": "alejandro", "password": "12345", "properties": { "greeting": "Hola, Ale", "year_born": 1980, "hobbies": ["tacos", "pisto", "chicas" ] }}
        reg4 = self.is1.register(ale["username"],ale["password"],ale["properties"])

        cris = { "username": "cristina", "password": "54321", "properties": { "greeting": "Ce fac, Cris", "year_born": 1989, "hobbies": ["horses", "cats", "tuika" ]}}
        reg5 = self.is1.register(cris["username"],cris["password"],cris["properties"])

        self.assertEqual(reg1, john)
        self.assertEqual(reg2, mark)
        self.assertEqual(reg3, jack)
        self.assertEqual(reg4, ale)
        self.assertEqual(reg5, cris)


    def test_authenticate(self):

        john = { "username": "john", "password": "12345", "properties": { "greeting": "Ahoj, John", "year_born": 1985, "hobbies": ["cars", "music", "python" ]  }}
        self.is1.register(john["username"],john["password"],john["properties"])

        mark = { "username": "mark", "password": "12345", "properties": { "greeting": "Ahoj, Mark", "year_born": 1995, "hobbies": ["bike", "programming", "star wars" ] }}
        self.is1.register(mark["username"],mark["password"],mark["properties"])

        jack = { "username": "jack", "password": "54321", "properties": { "greeting": "Hello, Jack", "year_born": 1987, "hobbies": ["cars", "tea", "ruby" ] }}
        self.is1.register(jack["username"],jack["password"],jack["properties"])

        self.assertEqual(self.is1.authenticate("mark","12345"), True)
        self.assertEqual(self.is1.authenticate("mark","12346"), False)
        self.assertEqual(self.is1.authenticate("david","12346"), False)
        self.assertEqual(self.is1.authenticate("jack","54321"), True)

        # test case insensitivity
        self.assertEqual(self.is1.authenticate("mARk","12345"), True)
        self.assertEqual(self.is1.authenticate("jAcK","54321"), True)

    def test_save_json_creates_file(self):

        path = "users.json"
        # make sure users.json does not exist
        if os.path.isfile(path): os.remove(path)

        john = { "username": "john", "password": "12345", "properties": { "greeting": "Ahoj, John", "year_born": 1985, "hobbies": ["cars", "music", "python" ]  }}
        self.is1.register(john["username"],john["password"],john["properties"])

        mark = { "username": "mark", "password": "12345", "properties": { "greeting": "Ahoj, Mark", "year_born": 1995, "hobbies": ["bike", "programming", "star wars" ] }}
        self.is1.register(mark["username"],mark["password"],mark["properties"])

        with open(path,"w+") as f:
            self.is1.save_to_json(path, overwrite=True)

        try:
            with open(path) as f:
                f.readlines()
        except IOError:
            print("File not accessible")

    def test_save_json_throws_exception(self):

        path = "users.json"
        # make sure users.json does not exist
        if os.path.isfile(path): os.remove(path)

        john = { "username": "john", "password": "12345", "properties": { "greeting": "Ahoj, John", "year_born": 1985, "hobbies": ["cars", "music", "python" ]  }}
        self.is1.register(john["username"],john["password"],john["properties"])

        mark = { "username": "mark", "password": "12345", "properties": { "greeting": "Ahoj, Mark", "year_born": 1995, "hobbies": ["bike", "programming", "star wars" ] }}
        self.is1.register(mark["username"],mark["password"],mark["properties"])

        try:
            # make sure users.json exists
            with open(path,"w+") as f:
                f.write("hello world")

            self.is1.save_to_json(path, overwrite=False)

        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    def test_load_json_invalid_throws_exception(self):

        path = "users.json"
        # make sure users.json does not exist
        if os.path.isfile(path): os.remove(path)

        try:
            # make sure users.json exists
            with open(path,"w+") as f:
                f.write("{invalidJSON]]]")

            self.is1.load_to_json(path)

        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    def test_load_json_empty_success(self):

        path = "empty.txt"
        # make sure users.json does not exist
        if os.path.isfile(path): os.remove(path)

        self.is1.load_to_json(path)
        self.assertEqual(self.is1.data, {"identities": []})


    def test_load_json_valid_success(self):

        path = "users.json"
        # make sure users.json does not exist
        if os.path.isfile(path): os.remove(path)

        john = { "username": "john", "password": "12345", "properties": { "greeting": "Ahoj, John", "year_born": 1985, "hobbies": ["cars", "music", "python" ]  }}
        self.is1.register(john["username"],john["password"],john["properties"])

        with open(path,"w+") as f:
            f.write("""{
                "identities": [
                    {
                        "username": "mark",
                        "password": "12345",
                        "properties": []
                    }
                ]
            }""")

        self.is1.load_to_json(path)



if __name__ == "__main__":
    unittest.main()