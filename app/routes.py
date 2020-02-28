from app import app, db
from app.models import Employee, Department 
from flask import render_template, redirect, request
from sqlalchemy import update

@app.route('/')
def index():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('index.html', title="Home", employees=employees, departments=departments)

# show employees page
@app.route('/employees')
def show_employees():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('employees.html', title="Employees", employees=employees, departments=departments)



# add an employee
@app.route('/employees', methods=['GET', 'POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    department = request.form.get('department')
    # department = Department.query.filter_by(id=department_id).first() 
    newEmployee = Employee(first_name=first_name, last_name=last_name, department=department)
    db.session.add(newEmployee)
    db.session.commit()
    return redirect('/employees')

# edit an employee


# delete an employee (can we do this if the employee is in a department?)


# can we have a filter view of employees, showing employees by department? This isn't strictly necessary, as it does the same as having a separate departments page. but it would be useful to try to work out how to do it.


# show departments page
@app.route('/departments')
def show_departments():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('departments.html', title="Departments", departments=departments, employees=employees)

# add a department
@app.route('/departments', methods=['GET', 'POST'])
def add_department():
    # name = request.form['name']
    name = request.form.get('name')
    newDepartment = Department(name=name)
    db.session.add(newDepartment)
    db.session.commit()
    return redirect('/departments')


# edit a department
# @app.route('/departments/<int:department_id>/update', methods=['POST'])
# def update_department(department_id):
#     department = Department.query.get(department_id)
#     new_name = request.form.get('new_name')
#     department.done = True 
#     db.session.commit()
#     return redirect('/departments')

# separate function to edit the employees?
@app.route('/departments/<int:department_id>/add_employee', methods=['GET', 'POST'])
def add_employee_to_department(department_id, employee_id):
    employee_id = request.form.get("employee_id")
    department_id = request.form.get("department_id")
    department = Department.query.filter_by(id=department_id).first()
    employee = Employee.query.filter_by(id=employee_id).first()
    department.employees.append(employee) 
    db.session.commit()
    return redirect('/departments')


# delete a department (will this work if there are employees?)