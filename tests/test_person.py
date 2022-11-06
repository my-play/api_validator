import pytest
from src.person import build_person, get_person_age, get_person_gender, get_person_nationality
import names

number_of_persons = 5


def prepare_person():
    name = names.get_first_name()
    return build_person(name)


def prepare_expected_persons():
    persons = []
    for _ in range(number_of_persons):
        person = prepare_person()
        persons.append(person)
    return persons


#https://docs.pytest.org/en/6.2.x/parametrize.html
@pytest.mark.parametrize("expected_person", prepare_expected_persons())
def test_person_data_apis_consistency(expected_person):
    name = expected_person.get_name()
    actual_age = get_person_age(name)
    assert actual_age == expected_person.get_age()
    actual_gender = get_person_gender(name)
    assert actual_gender == expected_person.get_gender()
    actual_nationality = get_person_nationality(name)
    assert actual_nationality == expected_person.get_nationality()
    print("api's test consistency tests  passed ")
