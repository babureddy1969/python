from pytest1 import reverseString
import mock
import builtins
def test_reverseString_ok():
    with mock.patch.object(builtins, 'input', lambda _: '19'):
        assert reverseString() == '91'
# def test_function1():
#     pytest1.input=lambda:'1 2 3 4 5'
#     output = pytest1.reverseString(['a','b','c'])
#     assert output==[5,4,3,2,1]