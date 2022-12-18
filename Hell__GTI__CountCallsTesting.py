from main import CountCalls
import time
import timeit
import logging_TimeTrials
print("This Challenge is for myself to import. \n Goal One : Beat the Challenges 1-100 with python to the best of "
      "your ability \n Goal Two  : Beat the Challenges 1-100 with cython to the best of "
      "your ability\n GOOD LUCK YOU CAN DO IT.\n\n") #"This Challenge is for myself to import.#



"""Philosophy of This Project.
Enter A new grad With literally no idea what the shit to do with his life.
So this means just we do something, This is that something.     - {Rahenvy : Jose' Israel Ossorio-Rojas}""" #Philosophy of This Project


def test_compare(select_RangeValueFirst,select_RangeValueSecond):
    """Qestion One"""
    f1 = CountCalls().D7NM5(range(int(select_RangeValueFirst), int(select_RangeValueSecond)))
    if (x for x in f1 if x % 7 != 0 and x % 5 != 0):
        return AssertionError(f"your args return Incorrect {(x for x in f1 if f1 % 7 != 0 and f1 % 5 == 0)}")
    print(f"Final Result = {f1}")
    return f1


lowVal, highVals = input("Your low number?"), input("Your high number?")
starttime = timeit.default_timer()

Question_OneTestResults = {"Problem Number":"Question 1",
                "Test Start Time": str(time.asctime( time.localtime(time.time()) )),
               "Low Value": str(lowVal) ,
               "High Value": str(highVals) ,"Range":test_compare(lowVal, highVals),
               "Time Difference"  : timeit.default_timer() - starttime

               }

logging_TimeTrials.TimeTitals(Question_OneTestResults)
