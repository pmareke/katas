from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    name: str
    age: int


@dataclass
class EmployeeReport:
    employees: List[Employee]

    def employees_older_than_18(self) -> List[Employee]:
        return list(filter(lambda employee: employee.age >= 18, self.employees))

    def employees_sorted_by_name(self, descending: bool = False) -> List[Employee]:
        return self._sort_by_name(self.employees_older_than_18(), descending)

    def capitalize_names(self) -> List[Employee]:
        return list(
            map(
                lambda employee: self._create_capitalize_employee(employee),
                self.employees_sorted_by_name(),
            )
        )

    def _create_capitalize_employee(self, employee: Employee) -> Employee:
        return Employee(employee.name.capitalize(), employee.age)

    def _sort_by_name(
        self, valid_employees: List[Employee], descending: bool = False
    ) -> List[Employee]:
        return sorted(
            valid_employees,
            key=lambda employee: employee.name.lower(),
            reverse=descending,
        )
