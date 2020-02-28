from app import db
from app.models import Employee, Department

# clear the database
Employee.query.delete()
Department.query.delete()

# create employees
employee1 = Employee(first_name="Cantata ", last_name="Zomes")
employee2 = Employee(first_name="Louder", last_name="Fargo")
employee3 = Employee(first_name="Varius", last_name="Lant")

# create departments
department1 = Department(name="HR")
department2 = Department(name="Operations")
department3 = Department(name="Sales")

# add the employees and departments to the session
db.session.add(employee1)
db.session.add(employee2)
db.session.add(employee3)
db.session.add(department1)
db.session.add(department2)
db.session.add(department3)



# save (commit) the session
db.session.commit()
# print(employee3)

# add an employee to a department
department3.employees.append(employee3)
department3.employees.append(employee2)
department3.employees.append(employee1)

for employee in department3.employees:
    print(employee)