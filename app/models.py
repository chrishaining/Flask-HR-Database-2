from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64), index=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return '<Employee {} {}>'.format(self.first_name, self.last_name)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<{} Department>'.format(self.name)



