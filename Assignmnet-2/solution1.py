class Employee:
    def __init__(self):
        print('Employee created !!!')
    
    def __del__(self):
        print('Employee destructed !!!')
    
    def working(self):
        print('Employee is Working !!!')

employee1 = Employee()
employee1.working()

employee2 = Employee()
employee2.working()
