import time


def time_trial(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = start - end
        func_name = "{}".format(repr(func.__name__))
        refinshed = ("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))

        Question_OneTestResults = {
            "Problem Number": func_name,
            "Test Start Time": f"{start}",
            "Test Start end": f"{end}",
            "refinshed": f"{refinshed}",
            "Result": f"{result}",
        }
        return (Question_OneTestResults)

    return wrapper
