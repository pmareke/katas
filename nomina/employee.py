from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    salary: int

    @property
    def monthly_salary(self) -> float:
        return self.salary / 12
