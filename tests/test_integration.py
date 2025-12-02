
from calculator import Calculator

def test_sequence():
    calc = Calculator()
    result = calc.add(2, 3)
    result = calc.multiply(result, 4)
    assert result == 20
