from src.config.config import config

def test_user_age_is_42():
    assert user.age == 43

def test_user_age_is_50(user):
    assert user.age == 50

def test_():
    print(config.get("BASE_URL_API"))

def test_ui_POM():
    print(config.get("BASE_URL_API"))