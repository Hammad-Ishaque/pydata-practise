from abc import ABCMeta, abstractmethod


# What particular instance to create

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        """
        :return:
        """


class Student(IPerson):

    def __init__(self):
        self.name = "I am Student"

    def person_method(self):
        print("This is Student!")


class Teacher(IPerson):

    def __init__(self):
        self.name = "I am Teacher"

    def person_method(self):
        print("This is Teacher!")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        return -1


choice = input("What type of person do you want to create?\n")
person = PersonFactory.build_person(choice)
person.person_method()
