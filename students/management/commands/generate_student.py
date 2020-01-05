from students.models import Student
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create random students'

    def handle(self, **kwargs):

        for _ in range(100):
            Student.generate_student()