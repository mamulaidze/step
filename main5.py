import unittest

def get_allowed_users():
    return ["john", "jane", "bob", "alice"]

def register_user(username):
    return username.lower()


class TestUser(unittest.TestCase):

    def test_register_user(self):
        result = register_user("John")
        self.assertIn(result, get_allowed_users())

    def test_allowed_users(self):
        users = get_allowed_users()

        self.assertIn("john", users)
        self.assertIn("alice", users)
        self.assertNotIn("dato", users)


if __name__ == "__main__":
    unittest.main()