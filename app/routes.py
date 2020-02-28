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
    return render_template('employees.html', title="Employees", employees=employees)



# add an employee
@app.route('/employees', methods=['POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    newEmployee = Employee(first_name=first_name, last_name=last_name)
    db.session.add(newEmployee)
    db.session.commit()
    return redirect('/employees')

# edit an employee

# delete an employee (can we do this if the employee is in a department?)


# can we have a filter view of employees, showing employees by department? This isn't strictly necessary, as it does the same as having a separate departments page. but it would be useful to try to work out how to do it.


# show departments page
@app.route('/departments')
def show_departments():
    departments = Department.query.all()
    return render_template('departments.html', title="Departments", departments=departments)

# add a department
@app.route('/departments', methods=['POST'])
def add_department():
    name = request.form['name']
    newDepartment = Department(name=name)
    db.session.add(newDepartment)
    db.session.commit()
    return redirect('/departments')


# edit a department

# separate function to edit the employees?


# delete a department (will this work if there are employees?)