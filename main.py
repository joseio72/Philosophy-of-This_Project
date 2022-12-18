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

    def D7NM5(self,args):
        print(args)
        # Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
        if (x for x in args if x % 7 != 0 and x % 5 == 0) == True or (x for x in args if x % 7 == 0 and x % 5 == 0) == True :
            return AssertionError(f"your args return Incorrect {(x for x in args if x % 7 != 0 and x % 5 != 0)}")
        self.two_ThreeBoth = [x for x in args if x % 7 == 0 and x % 5 != 0]
        #print(self.two_ThreeBoth)
        return self.two_ThreeBoth

