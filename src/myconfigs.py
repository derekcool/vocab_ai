import configparser


configs = {}


def load_configs(filename):
    global configs
    config = configparser.ConfigParser()
    config.read(filename)
    for section in config.sections():
        options = config.options(section)
        for opt in options:
            value = config.get(section, opt)
            if opt == "debug":
                if value == "yes":
                    configs[opt] = True
                else:
                    configs[opt] = False
            else:
                configs[opt] = value
