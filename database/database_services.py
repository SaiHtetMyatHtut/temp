import sqlite3 as sql
import re


class Student_DB:

    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        con = sql.connect(self.db_name)
        cur = con.cursor()
        cur.execute(f"drop table if exists {table_name}")
        cur.execute(f"create table {table_name} (sid text, name text, phone text, address text)")
        con.commit()

    # def get_connection(self):
    #     return sql.connect(self.db_name)

    def add_student(self, sid, name, phone, address):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        cur.execute(f"insert into {self.table_name} values ('{sid}','{name}','{phone}','{address}')")
        con.commit()

    def get_student(self):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        students = cur.execute(f"select * from {self.table_name}").fetchall()
        con.commit()
        data = list()
        for x in students:
            data.append({"id": x[0], "name": x[1]})
        return data

    def get_student_id(self, *, name,):
        con = sql.connect(self.db_name)
        con.create_function('regexp', 2, lambda x, y: 1 if re.search(x, y) else 0)
        cur = con.cursor()
        students = cur.execute(f"select * from {self.table_name} where name REGEXP ?", [r'Thida\.*']).fetchone()
        con.commit()
        return students

    def remove_student(self, sid):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        status = cur.execute(f"delete from {self.table_name} where sid = '{sid}'").fetchall()
        con.commit()
        if not status:
            return "Failed to Delete Student or Student not exists"
        return "Successfully deleted"

    def update_student(self, *, sid, name=None):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        if not name:
            status = "Consider to add more parameters with column_name."
        else:
            data = cur.execute(f"select * from {self.table_name} where sid = '{sid}' ").fetchall()
            if not data:
                status = "Data not found."
            else:
                cur.execute(f"update {self.table_name} set name = '{name}' where sid = '{sid}'")
                status = "Updated Successfully"
        con.commit()
        return status
