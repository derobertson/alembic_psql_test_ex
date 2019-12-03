from sq_test import create_app
import os

app = create_app(os.environ.get('FLASK_ENV') or 'default')


