class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/db_dev'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/db_test'


def config(env):
    configs = {
        'development': Config,
        'testing': TestConfig,
        'default': Config
    }

    return configs.get(env) or configs['default']
