from . import CONN
from . import CURSOR

class Student:

    # --- MAGIC METHODS --- #

    def __init__(self, name, grade, id=None):
        self.name = name
        self.grade = grade
        self.id = id

    def __repr__(self):
        return f'Student(id={self.id}, name={self.name}, grade={self.grade})'

    # --- CLASS METHODS --- #

    # make a table if it doesn't exist
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRUMARY KEY, 
            name TEXT, 
            grade NUMBER
            )"""

        return CURSOR.execute(sql)
        

    # get all rows and map them into instances
    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM students"""

        student_tuple = CURSOR.execute(sql).fetchall()
        return [Student(name=student[1], grade=student[2], id=student[0]) for student in student_tuples]


    # get a row by id and map it into an instance
    @classmethod
    def get_by_id(cls, id):
        sql = """SELECT * FROM students
        WHERE id = ?
        """

        student_tuple = CURSOR.execute(sql, [id]).fetchone()
        return Student(name=student_tuple[1], grade=student_tuple[2], id=student_tuple[0])


    # def get_by_name(cls, name):
        sql = """SELECT * FROM students
        WHERE name = ?
        """

        student_tuple = CURSOR.execute(sql, [name]).fetchone()
        return Student(name=student_tuple[1], grade=student_tuple[2], id=student_tuple[0])


    # --- SQL METHODS --- #

    # add this to the database
    def create(self):
        sql = """INSERT INTO students (name, grade)
        VALUES (?, ?)
        """
        #(?) sanitates the data input
        
        CURSOR.execute(sql, [self.name, self.grade])
        CONN.commit()

        sql = """SELECT * FROM srudents
        WHERE id = last_insert_rowid()
        """

        student_tuple = CURSOR.execute(sql).fetchone()
        id = student_tuple[0]

        self.id = id 


    # save changes to the database
    def update(self):
        sql = """UPDATE students
        SET name = ?, grade = ?
        WHERE id = ?
        """

        CURSOR.execute(sql, [self.name, self,grade])
        CONN.commit()


    # remove from the database
    def destroy(self):
        sql = """DELETE FROM students
        WHERE name = ?
        """

        CURSOR.execute(sql, [self.name])
        CONN.commit()
