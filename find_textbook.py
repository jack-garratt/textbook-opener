import yaml

class FindTextbook():
    def __init__(self, navigator):
        self.__navigator = navigator
        with open("config.yaml") as config:
            try:
                self.__textbooks = yaml.safe_load(config)
            except yaml.YAMLError as exc:
                print(exc) 
    
    def get_textbooks(self):
        textbooks = []
        for textbook in self.__textbooks:
            textbooks.append(textbook)
        return textbooks

    def select_textbook(self, textbook):
        self.__navigator.click_link(self.__textbooks[textbook]["subject"])
        self.__navigator.click_link(self.__textbooks[textbook]["name"])