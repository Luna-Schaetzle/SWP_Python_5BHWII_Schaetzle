from graphviz import Digraph

# Initialisieren des Diagramms mit höherer Auflösung und ansprechenderem Layout
dot = Digraph(
    comment='UML Diagramm der Klassen',
    format='png',
    engine='dot'  # Du kannst auch 'fdp', 'sfdp', 'twopi', etc. ausprobieren
)

# Setzen der Graph-Attribute
dot.attr('graph', 
         dpi='500',  # Erhöht die Auflösung
         fontsize='12',
         fontname='Helvetica',
         rankdir='LR',  # Layout von links nach rechts
         splines='true',
         nodesep='1',
         ranksep='2'
        )

# Setzen der Node-Attribute
dot.attr('node',
         shape='record',
         style='filled,rounded',
         fillcolor='#f9f9f9',
         fontname='Helvetica',
         fontsize='10',
         color='#333333'
        )

# Setzen der Edge-Attribute
dot.attr('edge',
         fontname='Helvetica',
         fontsize='9',
         color='#555555'
        )

# Definition der Klassen mit ihren Attributen und Methoden
classes = {
    "Person": {
        "attributes": ["+ name: str", "+ age: int", "+ gender: str"],
        "methods": ["+ __init__(name, age, gender)", "+ show()"]
    },
    "Employee": {
        "attributes": ["+ department: str"],
        "methods": ["+ __init__(name, age, gender, department)", "+ show()"]
    },
    "HeadOfDepartment": {
        "attributes": [],
        "methods": ["+ __init__(name, age, gender, department)", "+ show()"]
    },
    "Department": {
        "attributes": ["+ name: str", "+ employees: List[Employee]", "+ head_of_department: HeadOfDepartment"],
        "methods": ["+ __init__(name, head_of_department)", "+ show()"]
    },
    "Company": {
        "attributes": ["+ name: str", "+ departments: List[Department]"],
        "methods": [
            "+ __init__(name)",
            "+ add_department(department)",
            "+ add_employee(department, employee)",
            "+ add_head_of_department(department, head_of_department)",
            "+ show_Departments()",
            "+ show_Employees()",
            "+ show_HeadOfDepartments()",
            "+ show_biggest_department()",
            "+ show_gender_equalety_percentage()",
            "+ _get_all_employees()",
            "+ _count_genders(employees)",
            "+ _print_gender_percentage(gender_count, total_employees)"
        ]
    },
    "main": {
        "attributes": [],
        "methods": ["+ main()"]
    }
}

# Definieren eines Farbschemas für die Klassen
color_scheme = {
    "Person": "#AED6F1",
    "Employee": "#A3E4D7",
    "HeadOfDepartment": "#F9E79F",
    "Department": "#F5B7B1",
    "Company": "#D2B4DE",
    "main": "#F7DC6F"
}

# Hinzufügen der Klassen zum Diagramm mit individuellen Farben
for class_name, details in classes.items():
    label = f"{{ {class_name} | " + "\\l".join(details["attributes"]) + " | " + "\\l".join(details["methods"]) + " \\l }}"
    dot.node(class_name, label=label, fillcolor=color_scheme.get(class_name, "#FFFFFF"))

# Definieren der Vererbungsbeziehungen mit spezifischen Farben und Stilen
dot.edge("Employee", "Person", arrowhead="onormal", style="solid", color="#1F618D")
dot.edge("HeadOfDepartment", "Employee", arrowhead="onormal", style="solid", color="#1F618D")

# Definieren der Assoziationen mit spezifischen Farben und Stilen
dot.edge("Department", "HeadOfDepartment", label="has", arrowhead="vee", style="dashed", color="#117A65")
dot.edge("Department", "Employee", label="has", arrowhead="vee", style="dashed", color="#117A65")
dot.edge("Company", "Department", label="contains", arrowhead="vee", style="dashed", color="#117A65")

# Optional: Hinzufügen von Abhängigkeiten (z.B. main hängt von Company) mit spezifischen Farben und Stilen
dot.edge("main", "Company", label="uses", arrowhead="vee", style="dotted", color="#AF7AC5")

# Speichern und Rendern des Diagramms
dot.render('uml_diagramm', view=True)
