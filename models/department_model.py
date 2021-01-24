from config import mysql


class DepartmentModel(object):

    @staticmethod
    def get_all_departments() -> list:
        dep_list = []
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM departments ORDER BY id')
        for row  in cursor.fetchall():
            dep_list.append({
                'id':row[0],
                'name':row[1]
                })
        return dep_list

    @staticmethod
    def get_depname_by_id(dep_id: int) -> str:
        cursor = mysql.get_db().cursor()
        query = 'SELECT name FROM departments WHERE id=%s'
        cursor.execute(query, (dep_id,))
        row = cursor.fetchone()

        #Сценарий извлечения названия департамента по Id
        return row[0]