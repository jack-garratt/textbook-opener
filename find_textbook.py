import yaml
from paths import get_resource

class FindTextbook():
    def __init__(self, navigator):
        self._navigator = navigator
        self._textbooks = self._get_textbooks()

    def _get_textbooks(self):
        with open(get_resource("config.yaml")) as config:
            try:
                textbooks = yaml.safe_load(config)
            except yaml.YAMLError as exc:
                print(exc) 
                textbooks = {}
        return textbooks


    def select_textbook(self, textbook):
        self._navigator.click_link(self._textbooks[textbook]["subject"])
        self._navigator.click_link(self._textbooks[textbook]["name"])


def get_textbooks_list():
    with open(get_resource("config.yaml")) as config:
        try:
            textbooks = list((yaml.safe_load(config)).keys())
        except yaml.YAMLError as exc:
            print(exc) 
            textbooks = []
    return textbooks

