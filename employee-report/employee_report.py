from dataclasses import dataclass


@dataclass
class Employee:
    _ADULT_AGE = 18
    name: str
    age: int

    def is_an_adult(self) -> bool:
        return self.age >= self._ADULT_AGE


@dataclass
class EmployeeReport:
    employees: list[Employee]

    def employees_allowed_to_work_on_sundays(self) -> list[Employee]:
        return list(
            filter(lambda employee: employee.is_an_adult(), self.employees))

    def employees_sorted_by_name(self,
                                 descending: bool = False) -> list[Employee]:
        return self._sort_by_name(self.employees_allowed_to_work_on_sundays(),
                                  descending)

    def capitalize_names(self) -> list[Employee]:
        return list(
            # pylint: disable=W0108
            map(
                lambda employee: self._create_capitalize_employee(employee),
                self.employees_sorted_by_name(),
            ))

    def _create_capitalize_employee(self, employee: Employee) -> Employee:
        return Employee(employee.name.capitalize(), employee.age)

    def _sort_by_name(self,
                      valid_employees: list[Employee],
                      descending: bool = False) -> list[Employee]:
        return sorted(
            valid_employees,
            key=lambda employee: employee.name.lower(),
            reverse=descending,
        )
