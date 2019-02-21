#
# This file will contain ways to reach the next as well as getting its attributes
# Attributes include : -
# 1) Name
# 2) Times used in File
# 3) Places Called in
# 4) Declaration Line
# 5) Number of Parameters

EMPTY_STRING = "NA"
EMPTY_NUM = -1
ERROR_STRING = "ERR"
ERROR_NUM = -2


# Function class with different attributes
class Function:

    # __init__ function the creates the object with file parameter
    def __init__(self, filePath, fromFunction):

        # filled usable variables
        self.filePath = filePath
        self.fromFunction = fromFunction
        self.fileList = self.__get_file_in_list()

        # variables that need to be filled
        self.name = EMPTY_STRING
        self.functionStart = EMPTY_NUM

    #
    # get the file in a list of lines
    #
    def __get_file_in_list(self):
        return [line for line in open(self.filePath)]

    #
    # get the lines where the function exist
    #
    def __get_function_start(self):

        # check if already called
        if self.functionStart != EMPTY_NUM:
            return EMPTY_NUM

        # go through the rest of the file and find "def"
        for index, line in enumerate(self.fileList):

            # ignoring lines that we already read
            if index < self.fromFunction:
                continue

            # finding function declaration
            if "def" in line.split():
                self.functionStart = index
                return index

        return ERROR_NUM

    #
    # get the name of the function
    #
    def get_name(self):

        # check if already called
        if(self.name != EMPTY_STRING):
            return self.name

        # getting the line with the function definition
        line = self.fileList[self.__get_function_start()]

        # getting rid of irrelevant info
        line = line.replace("("," ").replace(":", " ").split()

        # error case
        if(len(line) < 1):
            return ERROR_STRING

        # first should be "def"
        self.name = line[1]

        return line[1]

