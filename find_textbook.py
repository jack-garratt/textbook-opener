import yaml

class FindTextbook():
    def __init__(self, navigator):
        self.__navigator = navigator
        with open("config.yaml") as config:
            try:
                self.__textbooks = yaml.safe_load(config)
            except yaml.YAMLError as exc:
                print(exc) 