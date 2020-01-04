class BaseModule(object):
    __author__ = None
    __options__ = None
    __info__ = None

    def __init__(self):
        pass
    def getOptions(self):
        return self.__options__

    def getInfo(self):
        return self.__info__

    def run(self):
        pass

    def setOption(self,key,value):
        self.__options__[key] = value