# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class CountCalls:

    def __init__(self, *args, **kwargs):
        self.use_CaseValueSubjectOne = args
        self.use_CaseValueSubjectTwo= kwargs



    """Qestion One"""

    def Q1(self,args):
        print(args)
        # Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
        if (x for x in args if x % 7 == 0 and x % 5 == 0) == True :
            return AssertionError(f"Main.py your args return Incorrect {(x for x in args if x % 7 != 0 and x % 5 != 0)}")
        self.two_ThreeBoth = [x for x in args if x % 7 == 0 and x % 5 != 0]
        return self.two_ThreeBoth


    """Qestion Two"""

    def Q2(self, args):
        #Question: Write a program which can compute the factorial of a given numbers.
        # The results should be printed in a comma-separated sequence on a single line. ___List___
        # Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
        # Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

        """Enter Recursive approach """
        def factorial(n):
            # single line to find factorial
            return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
        return factorial(args)


    """Qestion Three"""

    def Q3(self, args) -> dict:
        i = 0
       #Question: With a given integral number n,
        # write a program to generate a dictionary that contains (i, i*i) such that is an integral number
        # between 1 and n (both included). and then the program should print the dictionary.
        # Suppose the following input is supplied to the program: 8
        # Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
        # Hints: In case of input data being supplied to the question,
        # it should be assumed to be a console input. Consider use dict()
        dict = {}
        while args != i:
            i+=1
            dict[i]=i*i
        return dict


    """Qestion Four"""
    def Q4(self, args):
        #Quesion: Write a program which accepts a sequence of comma-separated numbers from console
        # and generate a list and a tuple which contains every number.
        # Suppose the following input is supplied to the program: 34,67,55,33,12,98
        # Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
        #Hints: In case of input data being supplied to the question,
        # it should be assumed to be a console input. tuple() method can convert list to tuple
        global tuple
        list = args.split(",") #list
        tuple = tuple(list)  #tuple
        return list ,tuple



    """Qestion Five"""
    def Q4(self, args):
        # Question: Define a class which has at least two methods:
        # getString: to get a string from console input printString: to print the string in upper case.
        # Also please include simple test function to test the class methods.
        # Use init method to construct some parameters
        global tuple
        list = args.split(",")  # list
        tuple = tuple(list)  # tuple
        return list, tuple








