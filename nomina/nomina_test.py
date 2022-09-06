from expects import equal, expect
from nomina import Employee, Nomina


class TestNomina:
    def test_calculates_the_monthly_salary(self) -> None:
        name = "Steve Harrington"
        id = 67563
        salary = 5000
        employee = Employee(id, name, salary)
        expect(Nomina.calculate(employee)).to(
            equal(f"id: {id}, name: {name}, month: {5000 / 12}")
        )
