from employee import Employee


if __name__ == "__main__":
    emp = Employee(age=30)

    print(emp.age)
    emp.EmployeeID()

    emp.age = 35
    print(emp.age)
