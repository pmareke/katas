from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    salary: int


class Nomina:
    @staticmethod
    def calculate(employee: Employee) -> str:
        return (
            f"id: {employee.id}, name: {employee.name}, month: {employee.salary / 12}"
        )
