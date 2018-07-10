class Publication:

    def __init__(self):

        self.__doi = None
        self.__title = None
        self.__is_open = False

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, doi):
        self.__doi = doi

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        self.__is_open = is_open