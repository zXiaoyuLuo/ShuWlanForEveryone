class Config():
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config: dict = eval(f.read())

    def __getitem__(self, item):
        if item in self.config.keys():
            return self.config[item]
        else:
            IndexError("Unknown config item '{}'".format(item))
            return None

    def __repr__(self):
        repr_str = "Config items:\n"
        for key in self.config.keys():
            repr_str += f"{key}\n"

        return repr_str

    def get_config(self):
        return self.config


