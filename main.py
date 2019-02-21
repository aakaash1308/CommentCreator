from functionFinder import Function

# a simple testing function that gets the first function name
def testing(filePath):

    # declaring Function object
    function1 = Function(filePath, 0)
    print(function1.get_name())

testing("testFiles/BasicTest.py")