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


