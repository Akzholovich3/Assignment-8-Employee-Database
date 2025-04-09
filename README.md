# Employee Database Management System

## Overview
This Python application manages employee data using SQLite database with CRUD operations (Create, Read, Update, Delete).


## Files
- `employee.py`: Employee entity class
- `employee_dao.py`: Data Access Object class for database operations
- `main.py`: Test implementation
- `employee_db.sqlite`: Employee database

## Sample Input/Output
### Insert Employee
```python
emp1 = Employee(name="Mederbek Suiunbekov", position="Devops Engineer", salary=75000.0, hire_date="2025-01-01")
emp_id = dao.insert(emp1)
print(f"Inserted employee with ID: {emp_id}")
```
```ssh
Inserted employee with ID: 1
```

### Get Employee by ID
```python
employee = dao.get_by_id(emp_id)
print("\nRetrieved employee by ID:")
print(employee)
```
```ssh
Retrieved employee by ID:
Employee(id=1, name=Mederbek Suiunbekov, position=Devops Engineer, salary=75000.0, hire_date=2025-01-01)
```

### Get All Employees
```python
print("\nAll employees:")
employees = dao.get_all()
for emp in employees:
    print(emp)
```
```ssh
All employees:
Employee(id=1, name=Mederbek Suiunbekov, position=Devops Engineer, salary=75000.0, hire_date=2025-01-01)
```

### Update Employee
```python
employee.name = "Meder Suiun uulu"
employee.set_salary(80000.0)
dao.update(employee)
print("\nAfter update:")
updated_emp = dao.get_by_id(emp_id)
print(updated_emp)
```
```ssh
After update:
Employee(id=1, name=Meder Suiun uulu, position=Devops Engineer, salary=80000.0, hire_date=2025-01-01)
```

### Delete Employee
```python
dao.delete(emp_id)
print("\nAfter deletion:")
employees = dao.get_all()
print("Remaining employees count:", len(employees))
```
```ssh
After deletion:
Remaining employees count: 0
```

### Usage Example 
```python
dao = EmployeeDAO()
emp = Employee(name="Mederbek Suiunbekov", position="Devops Engineer", salary=75000.0, hire_date="2025-01-01")
emp_id = dao.insert(emp)
employee = dao.get_by_id(emp_id)
employee.set_salary(80000.0)
print(employee.get_salary())
dao.close()
```
