# model_test.py
import pytest
from model import validate_username, validate_password  # Import the functions to be tested

# Fixture to provide test data for username
@pytest.fixture
def username_data():
    return [
        ("validUser1", True),   # Valid username
        ("short", False),       # Too short
        ("thisusernameiswaytoolong", False),  # Too long
        ("user_123", False),    # Invalid: contains special character
        ("valid123", True),     # Valid username
    ]

# Fixture to provide test data for passwords
@pytest.fixture
def password_data():
    return [
        ("Password123", True),       # Valid password
        ("password", False),         # No uppercase, no number
        ("PASSWORD123", False),      # No lowercase
        ("Pass123", False),          # Too short
        ("P@ssw0rd123", True),      # Invalid: contains special character
        ("ValidPass1", True),        # Valid password
    ]

# Parameterized tests for username validation
@pytest.mark.parametrize("username, expected", [
    ("validUser1", True),  
    ("short", False),       
    ("thisusernameiswaytoolong", False),  
    ("user_123", False),    
    ("valid123", True),     
])
def test_validate_username(username, expected):
    assert validate_username(username) == expected

# Parameterized tests for password validation
@pytest.mark.parametrize("password, expected", [
    ("Password123", True),       
    ("password", False),         
    ("PASSWORD123", False),      
    ("Pass123", False),          
    ("P@ssw0rd123", True),      
    ("ValidPass1", True),        
])
def test_validate_password(password, expected):
    assert validate_password(password) == expected

# Using fixture for username validation
def test_username_with_fixture(username_data):
    for username, expected in username_data:
        assert validate_username(username) == expected

# Using fixture for password validation
def test_password_with_fixture(password_data):
    for password, expected in password_data:
        assert validate_password(password) == expected

# Mark a test as expected to fail (xfail)
@pytest.mark.xfail
def test_invalid_username():
    assert validate_username("invalid@user") == True  # This will fail

# Skip a test that should not run in some conditions
@pytest.mark.skip(reason="Skipping this test as it's not relevant currently")
def test_skipped_password():
    assert validate_password("1234") == True  # Skipped
