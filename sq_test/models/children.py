from sq_test import db


class Child(db.Model):
    __tablename__ = 'child'

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
    parent = db.relationship('sq_test.models.parents.Parent', back_populates='children')
