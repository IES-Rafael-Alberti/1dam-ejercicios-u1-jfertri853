import pytest
from src.P1_10.factorial import factorial
from src.P1_10.factorial import factorial_str


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (1, "1! => 1 = 1"),
        (6, "6! => 6 x 5 x 4 x 3 x 2 x 1 = 720"),
        (3, "3! => 3 x 2 x 1 = 6"),
    ]
)
def test_factorial_str_params(input_n1, expected):
    assert factorial_str(int(input_n1)) == expected
