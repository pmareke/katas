from expects import equal, expect
from nomina.employee import Employee
from nomina.nomina import Nomina


class TestNomina:

    def test_calculates_the_monthly_salary(self) -> None:
        name = "Steve Harrington"
        employee_id = 67563
        salary = 5000
        employee = Employee(employee_id, name, salary)
        expect(Nomina.calculate(employee)).to(
            equal(
                f"employee_id: {employee_id}, name: {name}, month: {salary / 12}, insurance: 0, taxable: 0"
            ))

    def test_calculates_the_insurance_contributions(self) -> None:
        name = "Robin Buckley"
        employee_id = 54637
        salary = 9060
        employee = Employee(employee_id, name, salary)
        expect(Nomina.calculate(employee)).to(
            equal(
                f"employee_id: {employee_id}, name: {name}, month: {salary / 12}, insurance: {10.00}, taxable: 0"
            ))

    def test_calculates_the_taxable(self) -> None:
        name = "Robin Buckley"
        employee_id = 54637
        salary = 12000
        employee = Employee(employee_id, name, salary)
        expect(Nomina.calculate(employee)).to(
            equal(
                f"employee_id: {employee_id}, name: {name}, month: {salary / 12}, insurance: {39.40}, taxable: {83.33}"
            ))
