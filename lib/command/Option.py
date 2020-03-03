class Option(dict):
    def __init__(self,args,necessity,description):
        self.args = args
        self.necessity = necessity
        self.description = description

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass
