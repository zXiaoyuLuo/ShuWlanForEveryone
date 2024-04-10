from model.config import Config
from model.auto_login import Auto_login as Login


def test():
    config_path = 'user.config'
    config = Config(config_path)

    action = Login(config)
    action.login()
