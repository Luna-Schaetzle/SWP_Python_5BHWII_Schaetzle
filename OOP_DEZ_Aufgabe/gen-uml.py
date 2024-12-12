import subprocess

uml_code = """
@startuml
class Person {
    +name: str
    +age: int
    +gender: str
    +__init__(name, age, gender)
    +show()
}

class Employee {
    +department: str
    +__init__(name, age, gender, department)
    +show()
}

class HeadOfDepartment {
    +__init__(name, age, gender, department)
    +show()
}

class Department {
    +name: str
    +employees: List[Employee]
    +head_of_department: HeadOfDepartment
    +__init__(name, head_of_department)
    +show()
}

class Company {
    +name: str
    +departments: List[Department]
    +__init__(name)
    +add_department(department)
    +add_employee(department, employee)
    +add_head_of_department(department, head_of_department)
    +show_Departments()
    +show_Employees()
    +show_HeadOfDepartments()
    +show_biggest_department()
    +show_gender_equalety_percentage()
    +_get_all_employees()
    +_count_genders(employees)
    +_print_gender_percentage(gender_count, total_employees)
}

class main {
    +main()
}

Employee --|> Person
HeadOfDepartment --|> Employee
Department "1" -- "many" Employee : has
Department "1" -- "1" HeadOfDepartment : has
Company "1" -- "many" Department : contains
main --> Company : uses
@enduml
"""

with open('diagram.puml', 'w') as file:
    file.write(uml_code)

# PlantUML ausführen, um das Diagramm zu generieren
subprocess.run(['plantuml', 'diagram.puml'])
