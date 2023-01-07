class CountCalls:

    def __init__(self, *args, **kwargs):
        self.use_CaseValueSubjectOne = args
        self.use_CaseValueSubjectTwo = kwargs


    """Qestion One"""
    def Q1(self, args):
        print(args)
        if (x for x in args if x % 7 == 0 and x % 5 == 0) == True:
            return AssertionError(
                f"Main.py your args return Incorrect {(x for x in args if x % 7 != 0 and x % 5 != 0)}")
        self.two_ThreeBoth = [x for x in args if x % 7 == 0 and x % 5 != 0]
        return self.two_ThreeBoth


    """Qestion Two"""
    def Q2(self, args):
        """Enter Recursive approach """
        def factorial(n):
            # single line to find factorial
            return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
        return factorial(args)


    """Qestion Three"""
    def Q3(self, args) -> dict:
        i = 0
        dict = {}
        while args != i:
            i += 1
            dict[i] = i * i
        return dict


    """Qestion Four"""
    def Q4(self, args):
        global tuple
        list = args.split(",")  # list
        tuple = tuple(list)  # tuple
        return list, tuple

    """Qestion Five"""
    def Q5_getString(self) -> str:
        string_to_print = input("Enter String : ")
        print(f'The Sting Entered {string_to_print}')
        return string_to_print

    def Q5_printString(self, args):
        args = args.upper()
        print(f'your args are now UpperCase {args}')
        return args


    """Qestion Six"""
    def Q6(self,args):
        import math
        print(args)
        def calc_Q(D)->list:
            C, H = 50, 30
            out= []
            for i in D:
              out.append(int(math.sqrt((2 * C * i) / H)))
            return out
        calc_Q(args)
        return calc_Q(i for i in args)


    """Qestion Eigth"""
    def Q8(self,args):
        strings = args.split(',')
        # Sort the list of strings alphabetically
        strings.sort()
        # Join the sorted list of strings into a single string with commas
        result = ','.join(strings)
        # Print the result
        return result

    """Qestion Nine"""
    def Q9(self, args):
        strings = args.upper()
        return strings

    """Qestion Ten"""
    def Q9(self, args):
        strings = args.upper()
        return strings
