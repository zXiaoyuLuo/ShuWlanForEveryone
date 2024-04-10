from auto_login import Auto_login
from config import Config


def main(config_path):
    config = Config(config_path)
    action = Auto_login(config)
    action.login()
