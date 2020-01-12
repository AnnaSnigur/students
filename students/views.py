from django.http import HttpResponse
from django.shortcuts import render

def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')
