import pytest
from expects import equal, expect
from employee_report import Employee, EmployeeReport


class TestEmployeeReport:

    @pytest.fixture
    def employees(self) -> list[Employee]:
        return [
            Employee(name="max", age=17),
            Employee(name="Sepp", age=18),
            Employee(name="Nina", age=15),
            Employee(name="mike", age=51),
        ]

    def test_list_of_all_employees_who_are_allowed_to_work_on_sundays(
            self, employees: list[Employee]) -> None:
        employee_report = EmployeeReport(employees)

        valid_employees = employee_report.employees_allowed_to_work_on_sundays()

        expect(len(valid_employees)).to(equal(2))
        expect(valid_employees).to(equal([employees[1], employees[3]]))

    def test_list_of_employees_sorted_by_their_name(
            self, employees: list[Employee]) -> None:
        employee_report = EmployeeReport(employees)

        valid_employees = employee_report.employees_sorted_by_name()

        expect(len(valid_employees)).to(equal(2))
        expect(valid_employees).to(equal([employees[3], employees[1]]))

    def test_list_of_employees_with_capitalize_name(
            self, employees: list[Employee]) -> None:
        employee_report = EmployeeReport(employees)

        valid_employees = employee_report.capitalize_names()

        for employee in valid_employees:
            expect(employee.name).to(equal(employee.name.capitalize()))

    def test_list_of_employees_sorted_by_their_name_in_descending_order(
            self, employees: list[Employee]) -> None:
        employee_report = EmployeeReport(employees)

        valid_employees = employee_report.employees_sorted_by_name(
            descending=True)

        expect(len(valid_employees)).to(equal(2))
        expect(valid_employees).to(equal([employees[1], employees[3]]))
