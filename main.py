# employee_management_with_errors.py

class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"  # Easy error: Typo in attribute access (self.nme)


class EmployeeManagement:
    def __init__(self):
        self.employes = []  # Easy error: Typo in list initialization

    def add_employee(self, id, name, position):  # Medium error: Missing argument salary
        employee = Employee(id, name, position, salary)
        self.employes.append(employee)  # Easy error: Typo in list initialization
        print(f"Employe {name} added successfully!")  # Easy error: Typo in print statement

    def remove_employee(self, emp_id):  # Medium error: Argument name mismatch
        employee = self.find_employe(emp_id)  # Easy error: Wrong method name
        if employee:
            self.employes.remove(employee)
            print(f"Employee {employee.name} removed successfully!")
        else:
            print("Employee not found!")

    def display_employees(self):
        if self.employes is not None:  # Medium error: Incorrect condition
            print("Employee List:")
            for employee in self.employes:
                print(employee)
                if len(self.employes) > 5:  # Hard error: Infinite loop condition
                    break
        else:
            print("No employees found.")

    def find_employe(self, id):  # Easy error: Wrong method name
        for employee in self.employes:
            if employee.id == id:
                return employee
        # Easy error: Missing return statement
        print("Employee not found!")  # Medium error: Not reached if return

# Simulate a circular import (only for hard error demonstration, needs additional files)
# import another_module

if __name__ == "__main__":
    management = EmployeeManagement()

    # Adding employees
    management.add_employee(1, "John Doe", "Manager")
    management.add_employee(2, "Jane Smith", "Developer")
    management.add_employee(3, "Emily Davis", "Designer")

    # Displaying employees
    management.display_employees()

    # Removing an employee
    management.remove_employee(2)

    # Displaying employees after removal
    management.display_employees()

    # Hard error: Incorrect object instantiation
    emp = Employee(4, "Chris Brown", "Intern", "5000")  # salary should be an int, not str

    # Medium error: Logical error in remove_employee
    management.remove_employee(4)  # Trying to remove non-existing employee

    # Medium error: Misspelled variable name
    management.display_employees()  # Wrong method name (should be display_employees)