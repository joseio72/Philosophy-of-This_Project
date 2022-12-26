from main import CountCalls
from logging_TimeTrials import time_trial
import logging

logging.basicConfig(filename='100_PythonChallenging_LOG.log', encoding='utf-8', level=logging.INFO)
print("This Challenge is for myself to import. \n Goal One : Beat the Challenges 1-100 with python to the best of "
      "your ability \n Goal Two  : Beat the Challenges 1-100 with cython to the best of "
      "your ability\n GOOD LUCK YOU CAN DO IT.\n\n") #"This Challenge is for myself to import.#



"""Philosophy of This Project.
Enter A new grad With literally no idea what the shit to do with his life.
So this means just we do something, This is that something.     - {Rahenvy : Jose' Israel Ossorio-Rojas}""" #Philosophy of This Project



class Level_3_Advanced:

    def test_compare_Q1(self):
        """Qestion One"""
        f1 = CountCalls().D7NM5(range(2000, 3200))
        if not (x for x in f1 if x % 7 == 0 and x % 5== 0):
            return AssertionError(f"your args return Incorrect {(x for x in f1 if f1 % 7 != 0 and f1 % 5 == 0)}")
        return f1

    @time_trial

    def test_compare_Q2(self):
        """Qestion One"""
        f2 = CountCalls().Q2(8)
        if f2 != 40320:
            return AssertionError("your args return Incorrect {} secs".format(repr(f2.__name__)))
        return f2


result = Level_3_Advanced().test_compare_Q2()
print(f"Result {result}")
logging.info(str(result))



'''
    def test_compare_Q3(self):
        """Qestion three"""


        f3 = CountCalls().Q3()
        if "statement testing":
            return AssertionError(f"")
        return f3


    def test_compare_Q4(self):
        """Qestion four"""


        f4 = CountCalls().Q4()
        if "statement testing":
            return AssertionError(f"")
        return f4


def test_compare_Q5(self):
    """Qestion five"""


f5 = CountCalls().Q5()
if "statement testing":
    return AssertionError(f"")
return f5


def test_compare_Q6(self):
    """Qestion six"""


f6 = CountCalls().Q6()
if "statement testing":
    return AssertionError(f"")
return f6


def test_compare_Q7(self):
    """Qestion seven"""


f7 = CountCalls().Q7()
if "statement testing":
    return AssertionError(f"")
return f7


def test_compare_Q8(self):
    """Qestion eight"""


f8 = CountCalls().Q8()
if "statement testing":
    return AssertionError(f"")
return f8


def test_compare_Q9(self):
    """Qestion nine"""


f9 = CountCalls().Q9()
if "statement testing":
    return AssertionError(f"")
return f9


def test_compare_Q10(self):
    """Qestion ten"""


f10 = CountCalls().Q10()
if "statement testing":
    return AssertionError(f"")
return f10


def test_compare_Q11(self):
    """Qestion eleven"""


f11 = CountCalls().Q11()
if "statement testing":
    return AssertionError(f"")
return f11


def test_compare_Q12(self):
    """Qestion twelve"""


f12 = CountCalls().Q12()
if "statement testing":
    return AssertionError(f"")
return f12


def test_compare_Q13(self):
    """Qestion thirteen"""


f13 = CountCalls().Q13()
if "statement testing":
    return AssertionError(f"")
return f13


def test_compare_Q14(self):
    """Qestion fourteen"""


f14 = CountCalls().Q14()
if "statement testing":
    return AssertionError(f"")
return f14


def test_compare_Q15(self):
    """Qestion fifteen"""


f15 = CountCalls().Q15()
if "statement testing":
    return AssertionError(f"")
return f15


def test_compare_Q16(self):
    """Qestion sixteen"""


f16 = CountCalls().Q16()
if "statement testing":
    return AssertionError(f"")
return f16


def test_compare_Q17(self):
    """Qestion seventeen"""


f17 = CountCalls().Q17()
if "statement testing":
    return AssertionError(f"")
return f17


def test_compare_Q18(self):
    """Qestion eighteen"""


f18 = CountCalls().Q18()
if "statement testing":
    return AssertionError(f"")
return f18


def test_compare_Q19(self):
    """Qestion nineteen"""


f19 = CountCalls().Q19()
if "statement testing":
    return AssertionError(f"")
return f19


def test_compare_Q20(self):
    """Qestion twenty"""


f20 = CountCalls().Q20()
if "statement testing":
    return AssertionError(f"")
return f20


def test_compare_Q21(self):
    """Qestion twenty-one"""


f21 = CountCalls().Q21()
if "statement testing":
    return AssertionError(f"")
return f21


def test_compare_Q22(self):
    """Qestion twenty-two"""


f22 = CountCalls().Q22()
if "statement testing":
    return AssertionError(f"")
return f22


def test_compare_Q23(self):
    """Qestion twenty-three"""


f23 = CountCalls().Q23()
if "statement testing":
    return AssertionError(f"")
return f23


def test_compare_Q24(self):
    """Qestion twenty-four"""


f24 = CountCalls().Q24()
if "statement testing":
    return AssertionError(f"")
return f24


def test_compare_Q25(self):
    """Qestion twenty-five"""


f25 = CountCalls().Q25()
if "statement testing":
    return AssertionError(f"")
return f25


def test_compare_Q26(self):
    """Qestion twenty-six"""


f26 = CountCalls().Q26()
if "statement testing":
    return AssertionError(f"")
return f26


def test_compare_Q27(self):
    """Qestion twenty-seven"""


f27 = CountCalls().Q27()
if "statement testing":
    return AssertionError(f"")
return f27


def test_compare_Q28(self):
    """Qestion twenty-eight"""


f28 = CountCalls().Q28()
if "statement testing":
    return AssertionError(f"")
return f28


def test_compare_Q29(self):
    """Qestion twenty-nine"""


f29 = CountCalls().Q29()
if "statement testing":
    return AssertionError(f"")
return f29


def test_compare_Q30(self):
    """Qestion thirty"""


f30 = CountCalls().Q30()
if "statement testing":
    return AssertionError(f"")
return f30


def test_compare_Q31(self):
    """Qestion thirty-one"""


f31 = CountCalls().Q31()
if "statement testing":
    return AssertionError(f"")
return f31


def test_compare_Q32(self):
    """Qestion thirty-two"""


f32 = CountCalls().Q32()
if "statement testing":
    return AssertionError(f"")
return f32


def test_compare_Q33(self):
    """Qestion thirty-three"""


f33 = CountCalls().Q33()
if "statement testing":
    return AssertionError(f"")
return f33


def test_compare_Q34(self):
    """Qestion thirty-four"""


f34 = CountCalls().Q34()
if "statement testing":
    return AssertionError(f"")
return f34


def test_compare_Q35(self):
    """Qestion thirty-five"""


f35 = CountCalls().Q35()
if "statement testing":
    return AssertionError(f"")
return f35


def test_compare_Q36(self):
    """Qestion thirty-six"""


f36 = CountCalls().Q36()
if "statement testing":
    return AssertionError(f"")
return f36


def test_compare_Q37(self):
    """Qestion thirty-seven"""


f37 = CountCalls().Q37()
if "statement testing":
    return AssertionError(f"")
return f37


def test_compare_Q38(self):
    """Qestion thirty-eight"""


f38 = CountCalls().Q38()
if "statement testing":
    return AssertionError(f"")
return f38


def test_compare_Q39(self):
    """Qestion thirty-nine"""


f39 = CountCalls().Q39()
if "statement testing":
    return AssertionError(f"")
return f39


def test_compare_Q40(self):
    """Qestion forty"""


f40 = CountCalls().Q40()
if "statement testing":
    return AssertionError(f"")
return f40


def test_compare_Q41(self):
    """Qestion forty-one"""


f41 = CountCalls().Q41()
if "statement testing":
    return AssertionError(f"")
return f41


def test_compare_Q42(self):
    """Qestion forty-two"""


f42 = CountCalls().Q42()
if "statement testing":
    return AssertionError(f"")
return f42


def test_compare_Q43(self):
    """Qestion forty-three"""


f43 = CountCalls().Q43()
if "statement testing":
    return AssertionError(f"")
return ff45


def test_compare_Q46(self):
    """Qestion forty-six"""


f46 = CountCalls().Q46()
if "statement testing":
    return AssertionError(f"")
return f46


def test_compare_Q47(self):
    """Qestion forty-seven"""


f47 = CountCalls().Q47()
if "statement testing":
    return AssertionError(f"")
return f47


def test_compare_Q48(self):
    """Qestion forty-eight"""


f48 = CountCalls().Q48()
if "statement testing":
    return AssertionError(f"")
return f48


def test_compare_Q49(self):
    """Qestion forty-nine"""


f49 = CountCalls().Q49()
if "statement testing":
    return AssertionError(f"")
return f49


def test_compare_Q50(self):
    """Qestion fifty"""


f50 = CountCalls().Q50()
if "statement testing":
    return AssertionError(f"")
return f50


def test_compare_Q51(self):
    """Qestion fifty-one"""


f51 = CountCalls().Q51()
if "statement testing":
    return AssertionError(f"")
return f51


def test_compare_Q52(self):
    """Qestion fifty-two"""


f52 = CountCalls().Q52()
if "statement testing":
    return AssertionError(f"")
return f52


def test_compare_Q53(self):
    """Qestion fifty-three"""


f53 = CountCalls().Q53()
if "statement testing":
    return AssertionError(f"")
return f53


def test_compare_Q54(self):
    """Qestion fifty-four"""


f54 = CountCalls().Q54()
if "statement testing":
    return AssertionError(f"")
return f54


def test_compare_Q55(self):
    """Qestion fifty-five"""


f55 = CountCalls().Q55()
if "statement testing":
    return AssertionError(f"")
return f55


def test_compare_Q56(self):
    """Qestion fifty-six"""


f56 = CountCalls().Q56()
if "statement testing":
    return AssertionError(f"")
return f56


def test_compare_Q57(self):
    """Qestion fifty-seven"""


f57 = CountCalls().Q57()
if "statement testing":
    return AssertionError(f"")
return f57


def test_compare_Q58(self):
    """Qestion fifty-eight"""


f58 = CountCalls().Q58()
if "statement testing":
    return AssertionError(f"")
return f58


def test_compare_Q59(self):
    """Qestion fifty-nine"""


f59 = CountCalls().Q59()
if "statement testing":
    return AssertionError(f"")
return f59


def test_compare_Q60(self):
    """Qestion sixty"""


f60 = CountCalls().Q60()
if "statement testing":
    return AssertionError(f"")
return f60


def test_compare_Q61(self):
    """Qestion sixty-one"""


f61 = CountCalls().Q61()
if "statement testing":
    return AssertionError(f"")
return f61


def test_compare_Q62(self):
    """Qestion sixty-two"""


f62 = CountCalls().Q62()
if "statement testing":
    return AssertionError(f"")
return f62


def test_compare_Q63(self):
    """Qestion sixty-three"""


f63 = CountCalls().Q63()
if "statement testing":
    return AssertionError(f"")
return f63


def test_compare_Q64(self):
    """Qestion sixty-four"""


f64 = CountCalls().Q64()
if "statement testing":
    return AssertionError(f"")
return f64


def test_compare_Q65(self):
    """Qestion sixty-five"""


f65 = CountCalls().Q65()
if "statement testing":
    return AssertionError(f"")
return f65


def test_compare_Q66(self):
    """Qestion sixty-six"""


f66 = CountCalls().Q66()
if "statement testing":
    return AssertionError(f"")
return f66


def test_compare_Q67(self):
    """Qestion sixty-seven"""


f67 = CountCalls().Q67()
if "statement testing":
    return AssertionError(f"")
return f67


def test_compare_Q68(self):
    """Qestion sixty-eight"""


f68 = CountCalls().Q68()
if "statement testing":
    return AssertionError(f"")
return f68


def test_compare_Q69(self):
    """Qestion sixty-nine"""


f69 = CountCalls().Q69()
if "statement testing":
    return AssertionError(f"")
return f69


def test_compare_Q70(self):
    """Qestion seventy"""


f70 = CountCalls().Q70()
if "statement testing":
    return AssertionError(f"")
return f70


def test_compare_Q71(self):
    """Qestion seventy-one"""


f71 = CountCalls().Q71()
if "statement testing":
    return AssertionError(f"")
return f71


def test_compare_Q72(self):
    """Qestion seventy-two"""


f72 = CountCalls().Q72()
if "statement testing":
    return AssertionError(f"")
return f72


def test_compare_Q73(self):
    """Qestion seventy-three"""


f73 = CountCalls().Q73()
if "statement testing":
    return AssertionError(f"")
return f73


def test_compare_Q74(self):
    """Qestion seventy-four"""


f74 = CountCalls().Q74()
if "statement testing":
    return AssertionError(f"")
return f74


def test_compare_Q75(self):
    """Qestion seventy-five"""


f75 = CountCalls().Q75()
if "statement testing":
    return AssertionError(f"")
return f75


def test_compare_Q76(self):
    """Qestion seventy-six"""


f76 = CountCalls().Q76()
if "statement testing":
    return AssertionError(f"")
return f76


def test_compare_Q77(self):
    """Qestion seventy-seven"""


f77 = CountCalls().Q77()
if "statement testing":
    return AssertionError(f"")
return f77


def test_compare_Q78(self):
    """Qestion seventy-eight"""


f78 = CountCalls().Q78()
if "statement testing":
    return AssertionError(f"")
return f78


def test_compare_Q79(self):
    """Qestion seventy-nine"""


f79 = CountCalls().Q79()
if "statement testing":
    return AssertionError(f"")
return f79


def test_compare_Q80(self):
    """Qestion eighty"""


f80 = CountCalls().Q80()
if "statement testing":
    return AssertionError(f"")
return f80


def test_compare_Q81(self):
    """Qestion eighty-one"""


f81 = CountCalls().Q81()
if "statement testing":
    return AssertionError(f"")
return f81


def test_compare_Q82(self):
    """Qestion eighty-two"""


f82 = CountCalls().Q82()
if "statement testing":
    return AssertionError(f"")
return f82


def test_compare_Q83(self):
    """Qestion eighty-three"""


f83 = CountCalls().Q83()
if "statement testing":
    return AssertionError(f"")
return f83


def test_compare_Q84(self):
    """Qestion eighty-four"""


f84 = CountCalls().Q84()
if "statement testing":
    return AssertionError(f"")
return f84


def test_compare_Q85(self):
    """Qestion eighty-five"""


f85 = CountCalls().Q85()
if "statement testing":
    return AssertionError(f"")
return f85


def test_compare_Q86(self):
    """Qestion eighty-six"""


f86 = CountCalls().Q86()
if "statement testing":
    return AssertionError(f"")
return f86


def test_compare_Q87(self):
    """Qestion eighty-seven"""


f87 = CountCalls().Q87()
if "statement testing":
    return AssertionError(f"")
return f87


def test_compare_Q88(self):
    """Qestion eighty-eight"""


f88 = CountCalls().Q88()
if "statement testing":
    return AssertionError(f"")
return f88


def test_compare_Q89(self):
    """Qestion eighty-nine"""


f89 = CountCalls().Q89()
if "statement testing":
    return AssertionError(f"")
return f89


def test_compare_Q90(self):
    """Qestion ninety"""


f90 = CountCalls().Q90()
if "statement testing":
    return AssertionError(f"")
return f90


def test_compare_Q91(self):
    """Qestion ninety-one"""


f91 = CountCalls().Q91()
if "statement testing":
    return AssertionError(f"")
return f91


def test_compare_Q92(self):
    """Qestion ninety-two"""


f92 = CountCalls().Q92()
if "statement testing":
    return AssertionError(f"")
return f92


def test_compare_Q93(self):
    """Qestion ninety-three"""


f93 = CountCalls().Q93()
if "statement testing":
    return AssertionError(f"")
return f93


def test_compare_Q94(self):
    """Qestion ninety-four"""


f94 = CountCalls().Q94()
if "statement testing":
    return AssertionError(f"")
return f94


def test_compare_Q95(self):
    """Qestion ninety-five"""


f95 = CountCalls().Q95()
if "statement testing":
    return AssertionError(f"")
return f95


def test_compare_Q96(self):
    """Qestion ninety-six"""


f96 = CountCalls().Q96()
if "statement testing":
    return AssertionError(f"")
return f96


def test_compare_Q97(self):
    """Qestion ninety-seven"""


f97 = CountCalls().Q97()
if "statement testing":
    return AssertionError(f"")
return f97


def test_compare_Q98(self):
    """Qestion ninety-eight"""


f98 = CountCalls().Q98()
if "statement testing":
    return AssertionError(f"")
return f98


def test_compare_Q99(self):
    """Qestion ninety-nine"""


f99 = CountCalls().Q99()
if "statement testing":
    return AssertionError(f"")
return f99


def test_compare_Q100(self):
    """Qestion one hundred"""


f100 = CountCalls().Q100()
if "statement testing":
    return AssertionError(f"")
return f100


def test_compare_Q101(self):
    """Qestion one hundred and one"""


f101 = CountCalls().Q101()
if "statement testing":
    return AssertionError(f"")
return f101


def test_compare_Q102(self):
    """Qestion one hundred and two"""


f102 = CountCalls().Q102()
if "statement testing":
    return AssertionError(f"")
return f102


def test_compare_Q103(self):
    """Qestion one hundred and three"""


f103 = CountCalls().Q103()
if "statement testing":
    return AssertionError(f"")
return f103


def test_compare_Q104(self):
    """Qestion one hundred and four"""


f104 = CountCalls().Q104()
if "statement testing":
    return AssertionError(f"")
return f104


def test_compare_Q105(self):
    """Qestion one hundred and five"""


f105 = CountCalls().Q105()
if "statement testing":
    return AssertionError(f"")
return f105


def test_compare_Q106(self):
    """Qestion one hundred and six"""


f106 = CountCalls().Q106()
if "statement testing":
    return AssertionError(f"")
return f106


def test_compare_Q107(self):
    """Qestion one hundred and seven"""


f107 = CountCalls().Q107()
if "statement testing":
    return AssertionError(f"")
return f107


def test_compare_Q108(self):
    """Qestion one hundred and eight"""


f108 = CountCalls().Q108()
if "statement testing":
    return AssertionError(f"")
return f108


def test_compare_Q109(self):
    """Qestion one hundred and nine"""


f109 = CountCalls().Q109()
if "statement testing":
    return AssertionError(f"")
return f109


def test_compare_Q110(self):
    """Qestion one hundred and ten"""


f110 = CountCalls().Q110()
if "statement testing":
    return AssertionError(f"")
return f11043


def test_compare_Q44(self):
    """Qestion forty-four"""


f44 = CountCalls().Q44()
if "statement testing":
    return AssertionError(f"")
return f44


def test_compare_Q45(self):
    """Qestion forty-five"""


f45 = CountCalls().Q45()
if "statement testing":
    return AssertionError(f"")
return 

'''