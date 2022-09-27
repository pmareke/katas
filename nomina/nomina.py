from nomina.employee import Employee


class Nomina:

    @staticmethod
    def calculate(employee: Employee) -> str:
        insurance = 0 if employee.salary <= 8060 else (employee.salary -
                                                       8060) * 0.01
        taxable = 0 if employee.salary <= 11000 else (employee.salary -
                                                      11000) / 12
        return (f"employee_id: {employee.employee_id}, "
                f"name: {employee.name}, "
                f"month: {employee.monthly_salary}, "
                f"insurance: {insurance}, "
                "taxable: {0:.4g}".format(taxable))
