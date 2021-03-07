import yaml


def get_config(file="config.yml"):
    with open(file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


CONFIG = get_config()
