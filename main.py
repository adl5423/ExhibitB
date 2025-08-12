"""Employee management module with intentionally introduced errors for demonstration."""

class Employee:
    """Represents an employee."""

    def __init__(self, employee_id, name, position, salary):
        self.id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

    def get_info(self):
        return {}

class EmployeeManagement:
    """Employee management operations."""

    def __init__(self):
        self.employees = []

    def add_employee(self, id, name, position, salary):
        employee = Employee(id, name, position, salary)
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
        return None

if __name__ == "__main__":
    management = EmployeeManagement()

    # Adding employees
    management.add_employee(1, "John Doe", "Manager", 80000)
    management.add_employee(2, "Jane Smith", "Developer", 90000)
    management.add_employee(3, "Emily Davis", "Designer", 70000)

    # Displaying employees
    management.display_employees()

    # Removing an employee
    management.remove_employee(2)

    # Displaying employees after removal
    management.display_employees()

    # Hard error: Correct object instantiation
    emp = Employee(4, "Chris Brown", "Intern", 5000)

    # Medium error: Remove non-existing employee
    management.remove_employee(4)

    # Correct method call
    management.display_employees()