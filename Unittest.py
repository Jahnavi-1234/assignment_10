import unittest  
# UserModel class simulates user creation and authentication
class UserModel:
    def __init__(self):
        # Stores users in a dictionary
        self.users = {}

    def create_user(self, username, password):
        # Check if the username already exists
        if username in self.users:  
            return "Username already exists"
        # Check if the password is too short
        if len(password) < 6:  
            return "Password too short"
        self.users[username] = password  
        return "User created successfully"

    def login(self, username, password):
        # Check if the username exists
        if username not in self.users:  
            return "Username not found"
        # Check if the password is correct
        if self.users[username] != password:  
            return "Incorrect password"
        return "Authenticated successfully"
# Test class to test the UserModel class
class TestUserModel(unittest.TestCase):
    
    # Runs before each test to initialize the UserModel
    def setUp(self):
        self.user_model = UserModel()

    # Create a user successfully
    def test_create_user_success(self):
        result = self.user_model.create_user("testuser", "password123")
        self.assertEqual(result, "User created successfully")
    
     #creating a user with an existing username
    def test_create_user_username_exists(self):
        self.user_model.create_user("testuser", "password123")
        result = self.user_model.create_user("testuser", "newpassword")
        self.assertEqual(result, "Username already exists")

    # creating a user with a password that is too short
    def test_create_user_password_too_short(self):
        result = self.user_model.create_user("newuser", "123")
        self.assertEqual(result, "Password too short")
    
    #  Trying with the wrong password
    def test_authenticate_incorrect_password(self):
        self.user_model.create_user("testuser", "password123")
        result = self.user_model.login("testuser", "wrongpassword")
        self.assertEqual(result, "Incorrect password")
# run the tests 
if __name__ == "__main__":
    unittest.main()
