from faker import Faker
from django.db import models
from mimesis import Generic, Person
from datetime import datetime

'''
CREATE TABLE students_student (
    first_name varchar(20)
);
'''


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date = models.CharField(max_length=15)
    email = models.EmailField()
    telephone = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True, blank=True)

    @classmethod
    def generate_student(cls):
        fake = Faker()
        g = Generic('en')
        person = Person('en')
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date=g.datetime.date(),
            email=fake.email(),
            telephone=person.telephone(),
            address=fake.address(),
        )
        student.save()
        return student


class Group(models.Model):
    name_group = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5)
    specification = models.CharField(max_length=255)
