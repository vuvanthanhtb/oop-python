from employee import Employee
import employee_module

if __name__ == "__main__":

    # Class
    emp = Employee(age=30)
    print(emp.age)
    emp.EmployeeID()

    emp.age = 35
    print(emp.age)

    # Module
    employee_module.EmployeID()
    print(employee_module.employee)
    print(employee_module.employee["EmployeeId"])


# Note: Classes are preferred over modules because you can reuse them as they are and without much interference. 
# While with modules, you have only one with the entire program.
