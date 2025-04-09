# main.py
from employee import Employee
from employeeDAO import EmployeeDAO


def main():
    dao = EmployeeDAO()

    # Create and insert a new employee
    emp1 = Employee(name="Mederbek Suiunbekov", position="Devops Engineer", salary=75000.0, hire_date="2025-01-01")
    emp_id = dao.insert(emp1)
    print(f"Inserted employee with ID: {emp_id}")

    # Get employee by ID
    employee = dao.get_by_id(emp_id)
    print("\nRetrieved employee by ID:")
    print(employee)

    # Get all employees
    print("\nAll employees:")
    employees = dao.get_all()
    for emp in employees:
        print(emp)

    # Update employee
    employee.name = "Meder Suiun uulu"
    employee.set_salary(80000.0)
    dao.update(employee)
    print("\nAfter update:")
    updated_emp = dao.get_by_id(emp_id)
    print(updated_emp)

    # Delete employee
    dao.delete(emp_id)
    print("\nAfter deletion:")
    employees = dao.get_all()
    print("Remaining employees count:", len(employees))

    # Explicitly close the connection
    dao.close()


if __name__ == "__main__":
    main()
    