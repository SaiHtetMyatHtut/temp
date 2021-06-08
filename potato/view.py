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


def Home(request):
    return render(request, 'home.html')


def Result(request):
    name = request.POST.get("name")
    db = Student_DB(DB_NAME, STUDENT_TABLE)
    # ---
    db.add_student("S01", "Sai Htet Myat Htut", "09111222333", "Yangon")
    db.add_student("S02", "Thida Win", "09222333444", "Mandalay")
    db.add_student("S03", "Htet Myo San", "09333444555", "Taunggyi")
    db.add_student("S03", "Thura Khant Thein", "09555666777", "Yangon")
    # ---
    student = db.get_student_id(name=name)
    return render(request, 'result.html', {"name": student})
