from main import get_weather,add,divide,subtract
import pytest


def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(8) == "cool"

def test_add():
    assert add(1,2) == 3 ,"1+2 should be 3"
    assert add(-1,1) == 0, "-1+1 should be 3"
    assert add(0,0) == 0, "0+0 should be 0"

def test_divide():
    with pytest.raises(ZeroDivisionError,match="division by zero"):
        divide(10,0)


def test_subtract():
    assert subtract(10,1) == 9, "10-1 should be 0"
    assert subtract(0,9) == -9, "0-9 should be -9"