from sq_test.models import Parent
from sq_test import db
from . import main


@main.route('/')
def hello():
    return f'count: {db.session.query(Parent).count()}'
