from src.person import get_person_age


def test_get_age_api():
    name = "david"
    assert get_person_age(name) == 60
    print("age api test passed")



