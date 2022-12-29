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


    @time_trial
    def test_compare_Q1(self):
        """Qestion One"""
        f1 = CountCalls().D7NM5(range(2000, 3200))
        if not (x for x in f1 if x % 7 == 0 and x % 5== 0):
            return AssertionError(f"your args return Incorrect {(x for x in f1 if f1 % 7 != 0 and f1 % 5 == 0)}")
        return f1

    @time_trial
    def test_compare_Q2(self):
        """Qestion Two"""
        f2 = CountCalls().Q2(8)
        if f2 != 40320:
             raise AssertionError("func failed basic test.")
        return f2

    @time_trial
    def test_compare_Q3(self):
        """Qestion Three"""
        f3 = CountCalls().Q3(int(input("Q3, input a Whole number    ")))

        if type(f3) != dict:
            raise AssertionError("func failed basic test.")
        return f3

    @time_trial
    def test_compare_Q4(self):
        """Qestion Four"""
        f4_list , f4_tuple = CountCalls().Q4('34,67,55,33,12,98')
        print(type(f4_list))
        print(type(f4_tuple))

        #if not (not (type(f4_list)  list) and not (f4_tuple not tuple)):
            #raise AssertionError("func failed basic test.")
        return f4_list,f4_tuple

    @time_trial
    def test_compare_Q5(self):
        """Qestion five"""

        f5_getString = CountCalls().Q5_getString(None)
        f5_printString = CountCalls().Q5_printString(f5_getString.lower())
        return f5_printString


result = Level_3_Advanced().test_compare_Q5()
print(f"Result{result}")
logging.info(str(result))


'''
  @time_trial
def test_compare_Q6(self):
        """Qestion six"""
   f6 = CountCalls().Q6()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f6
result = Level_3_Advanced().test_compare_Q6()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q7(self):
        """Qestion seven"""
   f7 = CountCalls().Q7()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f7
result = Level_3_Advanced().test_compare_Q7()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q8(self):
        """Qestion eight"""
   f8 = CountCalls().Q8()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f8
result = Level_3_Advanced().test_compare_Q8()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q9(self):
        """Qestion nine"""
   f9 = CountCalls().Q9()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f9
result = Level_3_Advanced().test_compare_Q9()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q10(self):
        """Qestion ten"""
   f10 = CountCalls().Q10()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f10
result = Level_3_Advanced().test_compare_Q10()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q11(self):
        """Qestion eleven"""
   f11 = CountCalls().Q11()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f11
result = Level_3_Advanced().test_compare_Q11()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q12(self):
        """Qestion twelve"""
   f12 = CountCalls().Q12()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f12
result = Level_3_Advanced().test_compare_Q12()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q13(self):
        """Qestion thirteen"""
   f13 = CountCalls().Q13()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f13
result = Level_3_Advanced().test_compare_Q13()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q14(self):
        """Qestion fourteen"""
   f14 = CountCalls().Q14()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f14
result = Level_3_Advanced().test_compare_Q14()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q15(self):
        """Qestion fifteen"""
   f15 = CountCalls().Q15()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f15
result = Level_3_Advanced().test_compare_Q15()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q16(self):
        """Qestion sixteen"""
   f16 = CountCalls().Q16()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f16
result = Level_3_Advanced().test_compare_Q16()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q17(self):
        """Qestion seventeen"""
   f17 = CountCalls().Q17()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f17
result = Level_3_Advanced().test_compare_Q17()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q18(self):
        """Qestion eighteen"""
   f18 = CountCalls().Q18()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f18
result = Level_3_Advanced().test_compare_Q18()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q19(self):
        """Qestion nineteen"""
   f19 = CountCalls().Q19()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f19
result = Level_3_Advanced().test_compare_Q19()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q20(self):
        """Qestion twenty"""
   f20 = CountCalls().Q20()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f20
result = Level_3_Advanced().test_compare_Q20()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q21(self):
        """Qestion twenty-one"""
   f21 = CountCalls().Q21()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f21
result = Level_3_Advanced().test_compare_Q21()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q22(self):
        """Qestion twenty-two"""
   f22 = CountCalls().Q22()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f22
result = Level_3_Advanced().test_compare_Q22()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q23(self):
        """Qestion twenty-three"""
   f23 = CountCalls().Q23()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f23
result = Level_3_Advanced().test_compare_Q23()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q24(self):
        """Qestion twenty-four"""
   f24 = CountCalls().Q24()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f24
result = Level_3_Advanced().test_compare_Q24()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q25(self):
        """Qestion twenty-five"""
   f25 = CountCalls().Q25()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f25
result = Level_3_Advanced().test_compare_Q25()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q26(self):
        """Qestion twenty-six"""
   f26 = CountCalls().Q26()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f26
result = Level_3_Advanced().test_compare_Q26()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q27(self):
        """Qestion twenty-seven"""
   f27 = CountCalls().Q27()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f27
result = Level_3_Advanced().test_compare_Q27()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q28(self):
        """Qestion twenty-eight"""
   f28 = CountCalls().Q28()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f28
result = Level_3_Advanced().test_compare_Q28()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q29(self):
        """Qestion twenty-nine"""
   f29 = CountCalls().Q29()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f29
result = Level_3_Advanced().test_compare_Q29()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q30(self):
        """Qestion thirty"""
   f30 = CountCalls().Q30()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f30
result = Level_3_Advanced().test_compare_Q30()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q31(self):
        """Qestion thirty-one"""
   f31 = CountCalls().Q31()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f31
result = Level_3_Advanced().test_compare_Q31()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q32(self):
        """Qestion thirty-two"""
   f32 = CountCalls().Q32()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f32
result = Level_3_Advanced().test_compare_Q32()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q33(self):
        """Qestion thirty-three"""
   f33 = CountCalls().Q33()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f33
result = Level_3_Advanced().test_compare_Q33()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q34(self):
        """Qestion thirty-four"""
   f34 = CountCalls().Q34()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f34
result = Level_3_Advanced().test_compare_Q34()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q35(self):
        """Qestion thirty-five"""
   f35 = CountCalls().Q35()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f35
result = Level_3_Advanced().test_compare_Q35()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q36(self):
        """Qestion thirty-six"""
   f36 = CountCalls().Q36()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f36
result = Level_3_Advanced().test_compare_Q36()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q37(self):
        """Qestion thirty-seven"""
   f37 = CountCalls().Q37()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f37
result = Level_3_Advanced().test_compare_Q37()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q38(self):
        """Qestion thirty-eight"""
   f38 = CountCalls().Q38()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f38
result = Level_3_Advanced().test_compare_Q38()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q39(self):
        """Qestion thirty-nine"""
   f39 = CountCalls().Q39()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f39
result = Level_3_Advanced().test_compare_Q39()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q40(self):
        """Qestion forty"""
   f40 = CountCalls().Q40()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f40
result = Level_3_Advanced().test_compare_Q40()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q41(self):
        """Qestion forty-one"""
   f41 = CountCalls().Q41()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f41
result = Level_3_Advanced().test_compare_Q41()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q42(self):
        """Qestion forty-two"""
   f42 = CountCalls().Q42()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f42
result = Level_3_Advanced().test_compare_Q42()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q43(self):
        """Qestion forty-three"""
   f43 = CountCalls().Q43()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f43
result = Level_3_Advanced().test_compare_Q43()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q44(self):
        """Qestion forty-four"""
   f44 = CountCalls().Q44()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f44
result = Level_3_Advanced().test_compare_Q44()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q45(self):
        """Qestion forty-five"""
   f45 = CountCalls().Q45()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f45
result = Level_3_Advanced().test_compare_Q45()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q46(self):
        """Qestion forty-six"""
   f46 = CountCalls().Q46()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f46
result = Level_3_Advanced().test_compare_Q46()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q47(self):
        """Qestion forty-seven"""
   f47 = CountCalls().Q47()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f47
result = Level_3_Advanced().test_compare_Q47()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q48(self):
        """Qestion forty-eight"""
   f48 = CountCalls().Q48()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f48
result = Level_3_Advanced().test_compare_Q48()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q49(self):
        """Qestion forty-nine"""
   f49 = CountCalls().Q49()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f49
result = Level_3_Advanced().test_compare_Q49()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q50(self):
        """Qestion fifty"""
   f50 = CountCalls().Q50()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f50
result = Level_3_Advanced().test_compare_Q50()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q51(self):
        """Qestion fifty-one"""
   f51 = CountCalls().Q51()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f51
result = Level_3_Advanced().test_compare_Q51()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q52(self):
        """Qestion fifty-two"""
   f52 = CountCalls().Q52()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f52
result = Level_3_Advanced().test_compare_Q52()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q53(self):
        """Qestion fifty-three"""
   f53 = CountCalls().Q53()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f53
result = Level_3_Advanced().test_compare_Q53()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q54(self):
        """Qestion fifty-four"""
   f54 = CountCalls().Q54()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f54
result = Level_3_Advanced().test_compare_Q54()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q55(self):
        """Qestion fifty-five"""
   f55 = CountCalls().Q55()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f55
result = Level_3_Advanced().test_compare_Q55()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q56(self):
        """Qestion fifty-six"""
   f56 = CountCalls().Q56()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f56
result = Level_3_Advanced().test_compare_Q56()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q57(self):
        """Qestion fifty-seven"""
   f57 = CountCalls().Q57()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f57
result = Level_3_Advanced().test_compare_Q57()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q58(self):
        """Qestion fifty-eight"""
   f58 = CountCalls().Q58()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f58
result = Level_3_Advanced().test_compare_Q58()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q59(self):
        """Qestion fifty-nine"""
   f59 = CountCalls().Q59()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f59
result = Level_3_Advanced().test_compare_Q59()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q60(self):
        """Qestion sixty"""
   f60 = CountCalls().Q60()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f60
result = Level_3_Advanced().test_compare_Q60()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q61(self):
        """Qestion sixty-one"""
   f61 = CountCalls().Q61()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f61
result = Level_3_Advanced().test_compare_Q61()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q62(self):
        """Qestion sixty-two"""
   f62 = CountCalls().Q62()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f62
result = Level_3_Advanced().test_compare_Q62()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q63(self):
        """Qestion sixty-three"""
   f63 = CountCalls().Q63()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f63
result = Level_3_Advanced().test_compare_Q63()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q64(self):
        """Qestion sixty-four"""
   f64 = CountCalls().Q64()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f64
result = Level_3_Advanced().test_compare_Q64()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q65(self):
        """Qestion sixty-five"""
   f65 = CountCalls().Q65()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f65
result = Level_3_Advanced().test_compare_Q65()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q66(self):
        """Qestion sixty-six"""
   f66 = CountCalls().Q66()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f66
result = Level_3_Advanced().test_compare_Q66()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q67(self):
        """Qestion sixty-seven"""
   f67 = CountCalls().Q67()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f67
result = Level_3_Advanced().test_compare_Q67()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q68(self):
        """Qestion sixty-eight"""
   f68 = CountCalls().Q68()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f68
result = Level_3_Advanced().test_compare_Q68()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q69(self):
        """Qestion sixty-nine"""
   f69 = CountCalls().Q69()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f69
result = Level_3_Advanced().test_compare_Q69()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q70(self):
        """Qestion seventy"""
   f70 = CountCalls().Q70()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f70
result = Level_3_Advanced().test_compare_Q70()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q71(self):
        """Qestion seventy-one"""
   f71 = CountCalls().Q71()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f71
result = Level_3_Advanced().test_compare_Q71()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q72(self):
        """Qestion seventy-two"""
   f72 = CountCalls().Q72()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f72
result = Level_3_Advanced().test_compare_Q72()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q73(self):
        """Qestion seventy-three"""
   f73 = CountCalls().Q73()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f73
result = Level_3_Advanced().test_compare_Q73()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q74(self):
        """Qestion seventy-four"""
   f74 = CountCalls().Q74()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f74
result = Level_3_Advanced().test_compare_Q74()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q75(self):
        """Qestion seventy-five"""
   f75 = CountCalls().Q75()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f75
result = Level_3_Advanced().test_compare_Q75()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q76(self):
        """Qestion seventy-six"""
   f76 = CountCalls().Q76()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f76
result = Level_3_Advanced().test_compare_Q76()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q77(self):
        """Qestion seventy-seven"""
   f77 = CountCalls().Q77()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f77
result = Level_3_Advanced().test_compare_Q77()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q78(self):
        """Qestion seventy-eight"""
   f78 = CountCalls().Q78()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f78
result = Level_3_Advanced().test_compare_Q78()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q79(self):
        """Qestion seventy-nine"""
   f79 = CountCalls().Q79()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f79
result = Level_3_Advanced().test_compare_Q79()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q80(self):
        """Qestion eighty"""
   f80 = CountCalls().Q80()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f80
result = Level_3_Advanced().test_compare_Q80()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q81(self):
        """Qestion eighty-one"""
   f81 = CountCalls().Q81()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f81
result = Level_3_Advanced().test_compare_Q81()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q82(self):
        """Qestion eighty-two"""
   f82 = CountCalls().Q82()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f82
result = Level_3_Advanced().test_compare_Q82()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q83(self):
        """Qestion eighty-three"""
   f83 = CountCalls().Q83()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f83
result = Level_3_Advanced().test_compare_Q83()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q84(self):
        """Qestion eighty-four"""
   f84 = CountCalls().Q84()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f84
result = Level_3_Advanced().test_compare_Q84()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q85(self):
        """Qestion eighty-five"""
   f85 = CountCalls().Q85()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f85
result = Level_3_Advanced().test_compare_Q85()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q86(self):
        """Qestion eighty-six"""
   f86 = CountCalls().Q86()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f86
result = Level_3_Advanced().test_compare_Q86()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q87(self):
        """Qestion eighty-seven"""
   f87 = CountCalls().Q87()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f87
result = Level_3_Advanced().test_compare_Q87()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q88(self):
        """Qestion eighty-eight"""
   f88 = CountCalls().Q88()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f88
result = Level_3_Advanced().test_compare_Q88()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q89(self):
        """Qestion eighty-nine"""
   f89 = CountCalls().Q89()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f89
result = Level_3_Advanced().test_compare_Q89()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q90(self):
        """Qestion ninety"""
   f90 = CountCalls().Q90()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f90
result = Level_3_Advanced().test_compare_Q90()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q91(self):
        """Qestion ninety-one"""
   f91 = CountCalls().Q91()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f91
result = Level_3_Advanced().test_compare_Q91()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q92(self):
        """Qestion ninety-two"""
   f92 = CountCalls().Q92()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f92
result = Level_3_Advanced().test_compare_Q92()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q93(self):
        """Qestion ninety-three"""
   f93 = CountCalls().Q93()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f93
result = Level_3_Advanced().test_compare_Q93()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q94(self):
        """Qestion ninety-four"""
   f94 = CountCalls().Q94()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f94
result = Level_3_Advanced().test_compare_Q94()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q95(self):
        """Qestion ninety-five"""
   f95 = CountCalls().Q95()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f95
result = Level_3_Advanced().test_compare_Q95()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q96(self):
        """Qestion ninety-six"""
   f96 = CountCalls().Q96()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f96
result = Level_3_Advanced().test_compare_Q96()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q97(self):
        """Qestion ninety-seven"""
   f97 = CountCalls().Q97()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f97
result = Level_3_Advanced().test_compare_Q97()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q98(self):
        """Qestion ninety-eight"""
   f98 = CountCalls().Q98()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f98
result = Level_3_Advanced().test_compare_Q98()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q99(self):
        """Qestion ninety-nine"""
   f99 = CountCalls().Q99()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f99
result = Level_3_Advanced().test_compare_Q99()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q100(self):
        """Qestion one hundred"""
   f100 = CountCalls().Q100()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f100
result = Level_3_Advanced().test_compare_Q100()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q101(self):
        """Qestion one hundred and one"""
   f101 = CountCalls().Q101()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f101
result = Level_3_Advanced().test_compare_Q101()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q102(self):
        """Qestion one hundred and two"""
   f102 = CountCalls().Q102()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f102
result = Level_3_Advanced().test_compare_Q102()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q103(self):
        """Qestion one hundred and three"""
   f103 = CountCalls().Q103()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f103
result = Level_3_Advanced().test_compare_Q103()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q104(self):
        """Qestion one hundred and four"""
   f104 = CountCalls().Q104()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f104
result = Level_3_Advanced().test_compare_Q104()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q105(self):
        """Qestion one hundred and five"""
   f105 = CountCalls().Q105()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f105
result = Level_3_Advanced().test_compare_Q105()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q106(self):
        """Qestion one hundred and six"""
   f106 = CountCalls().Q106()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f106
result = Level_3_Advanced().test_compare_Q106()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q107(self):
        """Qestion one hundred and seven"""
   f107 = CountCalls().Q107()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f107
result = Level_3_Advanced().test_compare_Q107()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q108(self):
        """Qestion one hundred and eight"""
   f108 = CountCalls().Q108()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f108
result = Level_3_Advanced().test_compare_Q108()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q109(self):
        """Qestion one hundred and nine"""
   f109 = CountCalls().Q109()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f109
result = Level_3_Advanced().test_compare_Q109()
print(f"Result{result}")
logging.info(str(result))
  @time_trial
def test_compare_Q110(self):
        """Qestion one hundred and ten"""
   f110 = CountCalls().Q110()
   if 0 !=0 :
        raise AssertionError("func failed basic test.")
    return f110
result = Level_3_Advanced().test_compare_Q110()
print(f"Result{result}")
logging.info(str(result))


'''