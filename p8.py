class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_pay(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def yearly_pay(self):
        return super().yearly_pay() + self.bonus


staff = [
    Employee("Sara", 80000),
    Manager("Omar", 150000, 200000),
]

for person in staff:
    print(person.name, person.yearly_pay())

print(isinstance(staff[1], Employee))
