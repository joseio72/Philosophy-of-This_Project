from main import CountCalls
import timeit
import logging


print("This Challenge is for myself to import. \n Goal One : Beat the Challenges 1-100 with python to the best of "
      "your ability \n Goal Two  : Beat the Challenges 1-100 with cython to the best of "
      "your ability\n GOOD LUCK YOU CAN DO IT.") #"This Challenge is for myself to import.#



"""Philosophy of This Project.
Enter A new grad With literally no idea what the shit to do with his life.
So this means just we do something, This is that something.     - {Rahenvy : Jose' Israel Ossorio-Rojas}""" #Philosophy of This Project


def test_compare(select_RangeValueFirst,select_RangeValueSecond):
    """Qestion One"""
    select_RangeValue = CountCalls()
    f1 = select_RangeValue.D7NM5(range(int(select_RangeValueFirst), int(select_RangeValueSecond)))
    if (x for x in f1 if x % 7 != 0 and x % 5 == 0):
        return AssertionError(f"your args return Incorrect {(x for x in f1 if f1 % 7 != 0 and f1 % 5 == 0)}")
    print(f"Final Result = {select_RangeValue.D7NM5(range(select_RangeValueFirst, select_RangeValueSecond))}")


"""Qestion One"""
logging.basicConfig(filename='100_PythonChallenging_LOG.log', encoding='utf-8', level=logging.INFO)
lowVal, highVals = input("Your low number?"), input("Your high number?")
starttime = timeit.default_timer()
test_compare(lowVal,highVals)
endtime = timeit.default_timer()
serilizeItem= {"Test Start Time": str(starttime),
               "Low Value": str(lowVal) ,
               "High Value": str(highVals) ,
               "Time Difference"  : timeit.default_timer() - starttime
               }
logging.info(str(serilizeItem))
