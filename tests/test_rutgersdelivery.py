from rutgersdelivery.helpers import *

def test_password_true():
    assert validate_password("rurahrah") == True


def test_passsword_false():
    assert validate_password("peepeepoopoo") == False


