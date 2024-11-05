class Employee:
    def __init__(self):
       pass
    def calculate_salary(self):
        print('printing my salary')
class Manager(Employee):
    def __init__(self):
        pass
    def calculate_salary(self):
        basic_sal=20000
        int(basic_sal) ==(20,000)
        taxes = 5000
        int(taxes)==(5,000)
        gross_sal = (basic_sal)-(taxes)
        print(f'my salary is:,{gross_sal}')

employee = Employee()
manager = Manager()

employee.calculate_salary()
manager.calculate_salary()