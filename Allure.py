import pytest
import allure

def login(username, password):
    valid_username = "test_user"
    valid_password = "secure_password"
    return username == valid_username and password == valid_password

@allure.feature("Login Feature")
@allure.story("Valid Login")
def test_valid_login():
    with allure.step("Provide valid credentials"):
        username = "test_user"
        password = "secure_password"
    with allure.step("Call the login function"):
        result = login(username, password)
    with allure.step("Verify login result"):
        assert result, "Login should succeed with valid credentials"

@allure.feature("Login Feature")
@allure.story("Invalid Login")
@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("wrong_user", "secure_password", False),
        ("test_user", "wrong_password", False),
        ("wrong_user", "wrong_password", False),
    ],
)
def test_invalid_login(username, password, expected):
    with allure.step(f"Testing with username: {username}, password: {password}"):
        result = login(username, password)
    with allure.step("Verify login result"):
        assert result == expected, f"Expected {expected}, but got {result}"

@allure.feature("Login Feature")
@allure.story("Skipped Test")
@pytest.mark.skip
def test_skipped_case():
    assert False

@allure.feature("Login Feature")
@allure.story("Expected Failure")
@pytest.mark.xfail
def test_expected_failure():
    assert login("wrong_user", "secure_password")
