

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}')

class Employee(Person):
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender)
        self.department = department

    def show(self): 
        print(f'Department: {self.department}')
        super().show()

class HeadOfDepartment(Employee):
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender, department)

    def show(self):
        print('Head of Department')
        super().show()


class Department:
    def __init__(self, name, head_of_department):
        self.name = name
        self.employees = []
        self.head_of_department = head_of_department

    def show(self):
        print(f'Department: {self.name}')
        #self.head_of_department.show()

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def add_employee(self, department, employee):
        department.employees.append(employee)

    def add_head_of_department(self, department, head_of_department):
        department.head_of_department = head_of_department
    
    def show_Departments(self):
        for department in self.departments:
            department.show()
    
    def show_Employees(self):
        for department in self.departments:
            for employee in department.employees:
                employee.show()
    
    def show_HeadOfDepartments(self):
        for department in self.departments:
            department.head_of_department.show()
    
    def show_biggest_department(self):
        biggest_department = self.departments[0]
        for department in self.departments:
            if len(department.employees) > len(biggest_department.employees):
                biggest_department = department
        biggest_department.show()
    
    def show_gender_equalety_percentage(self):
        all_employees = self._get_all_employees()
        gender_count = self._count_genders(all_employees)
        self._print_gender_percentage(gender_count, len(all_employees))

    def _get_all_employees(self):
        all_employees = []
        for department in self.departments:
            all_employees += department.employees
            all_employees.append(department.head_of_department)
        return all_employees

    def _count_genders(self, employees):
        gender_count = {'male': 0, 'female': 0, 'other': 0}
        for employee in employees:
            if employee.gender.lower() in gender_count:
                gender_count[employee.gender.lower()] += 1
            else:
                gender_count['other'] += 1
        return gender_count

    def _print_gender_percentage(self, gender_count, total_employees):
        if total_employees == 0:
            print("No employees in the company.")
            return
        
        for gender, count in gender_count.items():
            percentage = (count / total_employees) * 100
            print(f'{gender.capitalize()} employees: {percentage:.2f}%')

# A few test cases in the main 

def main():
    # Create a company
    company = Company("Tech Solutions")

    # Create head of departments
    head_of_it = HeadOfDepartment("Alice", 45, "female", "IT")
    head_of_hr = HeadOfDepartment("Bob", 50, "non-binary", "HR")

    # Create departments
    it_department = Department("IT", head_of_it)
    hr_department = Department("HR", head_of_hr)

    # Add departments to the company
    company.add_department(it_department)
    company.add_department(hr_department)

    # Create employees
    emp1 = Employee("Charlie", 30, "female", "IT")
    emp2 = Employee("Diana", 28, "female", "IT")
    emp3 = Employee("Eve", 35, "other", "HR")
    emp4 = Employee("Frank", 40, "male", "HR")
    emp5 = Employee("George", 29, "male", "IT")
    emp6 = Employee("Hannah", 32, "female", "HR")
    emp7 = Employee("Ian", 27, "male", "IT")
    emp8 = Employee("Jane", 31, "female", "HR")
    emp9 = Employee("Karla", 22, "female" , "IT")


    # Add employees to departments
    company.add_employee(it_department, emp1)
    company.add_employee(it_department, emp2)
    company.add_employee(hr_department, emp3)
    company.add_employee(hr_department, emp4)
    company.add_employee(it_department, emp5)
    company.add_employee(hr_department, emp6)
    company.add_employee(it_department, emp7)
    company.add_employee(hr_department, emp8)
    company.add_employee(it_department, emp9)

    # Show all departments
    print("All Departments:")
    company.show_Departments()

    # Show all employees
    print("\nAll Employees:")
    company.show_Employees()

    # Show all heads of departments
    print("\nHeads of Departments:")
    company.show_HeadOfDepartments()

    # Show the biggest department
    print("\nBiggest Department:")
    company.show_biggest_department()

    # Show gender equality percentage
    print("\nGender Equality Percentage:")
    company.show_gender_equalety_percentage()


if __name__ == '__main__':
    main()












