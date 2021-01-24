from config import mysql


class EmployeeModel (object):

    @staticmethod
    def get_employees_by_department(dep_id: int) -> list:
        emp_list = []
        cursor = mysql.get_db().cursor()
        query = 'SELECT * FROM employees WHERE dep_id=%s'
        cursor.execute(query, (dep_id,))

        for row  in cursor.fetchall():
            emp_list.append({
                'id':row[0],
                'name':row[1],
                'age':row[2],
                'position':row[3],
                'salary':row[4],
                'dep_id':row[5]
                })


        return emp_list

    @staticmethod
    def add_employee(name: str, age: int, position: str, salary: float, dep_id: int) -> None:
        query = 'insert into employees (name, age, position, salary, dep_id) values (%s, %s, %s, %s, %s)'
        connection = mysql.get_db()
        cursor = connection.cursor()
        cursor.execute(query, (name, age, position, salary, dep_id))
        connection.commit()
