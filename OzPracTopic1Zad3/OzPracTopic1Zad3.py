
# Ќекоторые люди достига€ определенного возраста, в шутку празднуют только 20 или 21 день рождени€, навсегда. 
# — некоторыми математическими навыками это вполне возможно - нужно только выбрать правильную систему счислени€. 
# task_A342
# Ќаписать функцию happy_birthday(age), котора€ возвращает систему счислени€, 
# в которой данный возраст выгл€дит как 20 или 21.  
#  
# ѕример
# happy_birthday(32) ==> 16 -> 32(_в_10) == 20(_в_16)
# happy_birthday(39) ==> 19 -> 39(_в_10) == 21(_в_19)


import traceback


def happy_birthday(age):
    return age//2


# “есты
try:
    assert happy_birthday(32) == 16
    assert happy_birthday(39) == 19
    assert happy_birthday(65) == 32
    assert happy_birthday(83) == 41
    assert happy_birthday(22) == 11
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
