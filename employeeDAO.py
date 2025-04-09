import sqlite3
from employee import Employee


class EmployeeDAO:
    def __init__(self):
        self.conn = sqlite3.connect('employee_db.sqlite')
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                salary REAL NOT NULL,
                hire_date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert(self, employee):
        self.cursor.execute('''
            INSERT INTO employee (name, position, salary, hire_date)
            VALUES (?, ?, ?, ?)
        ''', (employee.name, employee.position, employee.get_salary(), employee.hire_date))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_by_id(self, id):
        self.cursor.execute('SELECT * FROM employee WHERE id = ?', (id,))
        row = self.cursor.fetchone()
        if row:
            emp = Employee(row[0], row[1], row[2], row[3], row[4])
            return emp
        return None

    def get_all(self):
        self.cursor.execute('SELECT * FROM employee')
        rows = self.cursor.fetchall()
        return [Employee(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    def update(self, employee):
        self.cursor.execute('''
            UPDATE employee 
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        ''', (employee.name, employee.position, employee.get_salary(), employee.hire_date, employee.id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete(self, id):
        self.cursor.execute('DELETE FROM employee WHERE id = ?', (id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.conn.close()