from main import get_weather,add,divide



def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(2) == "cool"

# def test_add():
#     assert add(1,2) == 3 ,
#     assert add(-1,1) == 0,
#     assert add(1,2) == 2 ,


