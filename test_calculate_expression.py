import pytest
from main import calculate_expression


def test_addition():
    assert calculate_expression("1+2+3+4") == 10
    assert calculate_expression("10+20+30") == 60
    assert calculate_expression("5+5+5+5") == 20


def test_subtraction():
    assert calculate_expression("10-2-3") == 5
    assert calculate_expression("20-10-5") == 5
    assert calculate_expression("100-50-25") == 25


def test_mixed_operations():
    assert calculate_expression("10+2-3+5") == 14
    assert calculate_expression("1-1+1-1+1") == 1
    assert calculate_expression("15+25-10+5") == 35


@pytest.mark.parametrize("expression", [
    "10+2a-3",
    "1+2-3-",
    "++1--2"
])
def test_invalid_input(expression):
    with pytest.raises(ValueError, match="Входная строка должна содержать только цифры, знаки '\\+' и '-'."):
        calculate_expression(expression)


if __name__ == "__main__":
    pytest.main()
