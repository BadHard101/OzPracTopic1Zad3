
# ��������� ���� �������� ������������� ��������, � ����� ��������� ������ 20 ��� 21 ���� ��������, ��������. 
# � ���������� ��������������� �������� ��� ������ �������� - ����� ������ ������� ���������� ������� ���������. 
# task_A342
# �������� ������� happy_birthday(age), ������� ���������� ������� ���������, 
# � ������� ������ ������� �������� ��� 20 ��� 21.  
#  
# ������
# happy_birthday(32) ==> 16 -> 32(_�_10) == 20(_�_16)
# happy_birthday(39) ==> 19 -> 39(_�_10) == 21(_�_19)


import traceback


def happy_birthday(age):
    return age//2


# �����
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
