class Employee:
    """A class describing an employee and it's salary."""

    def __init__(self, firstname, lastname, salary):
        """initialize attributes"""
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def describe_employee(self):
        employee = f"{self.lastname}, {self.firstname} - salary: ${self.salary:,}"
        return f"{employee.title()}"

    def give_raise(self, raise_by="5000"):
        self.new_salary = int(self.salary) + int(raise_by)
        self.salary = f"{self.new_salary:,}"


me = Employee("niclas", "behrendt", "500000")
print(me.describe_employee())
me.give_raise()
print(me.describe_employee())
