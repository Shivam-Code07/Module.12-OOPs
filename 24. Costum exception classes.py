class SalaryError(Exception):
    pass

def get_salary(salary):

    if salary < 0 :
        raise SalaryError("Salary can not be negative!!")
    else:
        bonus = 0.1 * salary
        return salary + bonus

salary = float(input("Enter the salary: "))
final_salary = get_salary(salary)
print(final_salary)