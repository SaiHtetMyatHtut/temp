import sqlite3

from django.shortcuts import render
from database.database_services import *
from home.widgets.forms import *
from django.http import HttpResponse

"""
print(db.remove_student(4))
print(db.update_student("S03"))
print(db.get_student())
print(db.get_student_id(sid="S01"))
db = Student_DB(DB_NAME, STUDENT_TABLE)
db.add_student('S01', 'Sai')
db.add_student('S02', 'Htet')
data = db.get_student()
"""

DB_NAME = "students.sqlite3"
STUDENT_TABLE = "student"

db = Student_DB(DB_NAME, STUDENT_TABLE)


def Home(request):
    return render(request, 'home.html')


def Result(request):
    name = request.POST.get("name")
    student = db.get_student_id(name=name)
    return render(request, 'result.html', {"name": student})


def Register(request):
    sid = request.POST.get("sid")
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    db.add_student(sid, name, phone, address)
    return render(request, 'register.html')


def Delete(request):
    sid = request.POST.get("sid")
    msg = db.remove_student(sid)
    return render(request, 'delete.html', {"message": msg})
