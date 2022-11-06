import json

import requests


class Person:
    def __init__(self, name, age, gender, nationality):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__nationality = nationality

    def __str__(self):
        return "name: " + self.__name + ", age: " + str(self.__age) + ", gender: " + self.__gender + ", nationality: " + self.__nationality

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_nationality(self):
        return self.__nationality


def build_person(name):
    person_age = get_person_age(name)
    person_gender = get_person_gender(name)
    person_nationality = get_person_nationality(name)
    return Person(name, person_age, person_gender, person_nationality)


def get_person_age(name):
    url = "https://api.agify.io?name=" + name
    response = requests.request('GET', url, verify=False)
    data = json.loads(response.text)
    age = data['age']
    # print(age)
    return age


def get_person_gender(name):
    url = "https://api.genderize.io?name="+name
    response = requests.request('GET', url, verify=False)
    data = response.json()
    gender = data['gender']
    # print(gender)
    return gender


def get_person_nationality(name):
    url = "https://api.nationalize.io?name="+name
    response = requests.request('GET', url, verify=False)
    data = response.json()
    countries = data['country']
    max_probability = 0
    country = None
    for current_country in countries:
        current_probability = current_country['probability']
        if float(current_probability) > max_probability:
            max_probability = current_probability
            country = current_country['country_id']
    # print(country)
    return country
