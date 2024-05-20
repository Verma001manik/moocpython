class Recording:
    def __init__(self, length):
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, len):
        if(len>=0):
            self.__length = len
        self.__length
the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)
