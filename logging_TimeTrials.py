import timeit
import logging
import Hell__GTI__CountCallsTesting


"""Qestion One"""
logging.basicConfig(filename='100_PythonChallenging_LOG.log', encoding='utf-8', level=logging.INFO)
lowVal, highVals = input("Your low number?"), input("Your high number?")
starttime = timeit.default_timer()
inter_CostumRange = Hell__GTI__CountCallsTesting.test_compare(lowVal, highVals)
endtime = timeit.default_timer()


Question_OneTestResults = {"Problem Number":"Question 1",
                "Test Start Time": str(starttime),
               "Low Value": str(lowVal) ,
               "High Value": str(highVals) ,"Range":inter_CostumRange,
               "Time Difference"  : timeit.default_timer() - starttime
               }
logging.info(str(Question_OneTestResults))
