class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        return self.base_salary + self.team_size * 5000


class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def calculate_salary(self):
        return self.base_salary + self.completed_projects * 10000


if __name__ == "__main__":
    employees = [
        Manager("Анна", 120000, team_size=5),
        Developer("Иван", 100000, completed_projects=3),
    ]
    for employee in employees:
        print(f"{employee.name}: {employee.calculate_salary():,.0f} руб.")
