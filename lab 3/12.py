class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)
        
class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + completed_projects * 500
        
class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
    
    def total_salary(self):
            return self.base_salary
    
command = input().split()

if command[0] == "Manager":
    name = command[1]
    base_salary = int(command[2])
    bonus_percent = int(command[3])
    employee = Manager(name, base_salary, bonus_percent)
elif command[0] == "Developer":
    name = command[1]
    base_salary = int(command[2])
    completed_projects = int(command[3])
    employee = Developer(name, base_salary, completed_projects)
else:
    name = command[1]
    base_salary = int(command[2])
    employee = Intern(name, base_salary)

print(f"Name: {employee.name}, Total: {employee.total_salary():.2f}")