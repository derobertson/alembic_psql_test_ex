from sq_test import db


class Parent(db.Model):
    __tablename__ = 'parent'

    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship('sq_test.models.children.Child', back_populates='parent')
