class Department:
    def __init__(self, department_name, description):
        self.department_name = department_name
        self.description = description

    def get_name(self):
        return self.department_name

    def get_description(self):
        return self.description

    def set_department_name(self, department_name):
        self.department_name = department_name

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f"{self.department_name} - {self.description}"
