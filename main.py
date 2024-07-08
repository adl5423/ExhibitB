```python
class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def get_salary(self, id):
        employee = self.find_employee(id)
        if employee:
            return employee.salary
        else:
            print("Employee not found!")
            return None

    def add_employee(self, employee_id, name, position, salary):
        employee = Employee(employee_id, name, position, salary)
        self.employees.append(employee)
        print(f"Employee {name} added successfully!")

    def remove_employee(self, emp_id):
        employee = self.find_employee(emp_id)
        if employee:
            self.employees.remove(employee)
            print(f"Employee {employee.name} removed successfully!")
        else:
            print("Employee not found!")

    def display_employees(self):
        if self.employees:
            print("Employee List:")
            for employee in self.employees:
                print(employee)
        else:
            print("No employees found.")

    def find_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        print("Employee not found!")

if __name__ == "__main__":
    management = EmployeeManagement()

    management.add_employee(1, "John Doe", "Manager", 75000)
    management.add_employee(2, "Jane Smith", "Developer", 65000)
    management.add_employee(3, "Emily Davis", "Designer", 60000)

    management.display_employees()

    management.remove_employee(2)

    management.display_employees()

    emp = Employee(4, "Chris Brown", "Intern", 5000)

    salary = management.get_salary(4)

    management.remove_employee(4)

    management.display_employees()
```