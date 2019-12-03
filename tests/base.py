from unittest import TestCase
from alembic.config import Config
from alembic.command import upgrade, downgrade
from sq_test import create_app, db


class BaseClass(TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.alembic_config = Config('alembic.ini')
        self.alembic_config.set_main_option('sqlalchemy.url', self.app.config['SQLALCHEMY_DATABASE_URI'])

        downgrade(self.alembic_config, revision='base')
        upgrade(self.alembic_config, revision='head')

        self.client = self.app.test_client()

    def tearDown(self) -> None:
        db.session.remove()
        self.app_context.pop()
