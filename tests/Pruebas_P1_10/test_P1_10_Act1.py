import pytest
from src.P1_10.P1_10_Act1 import numero_mayor


def test_numero_mayor():
    assert numero_mayor(1, 1) == 0
    assert numero_mayor(0, 0) == 0
    assert numero_mayor(100, -100) == 100
    assert numero_mayor(0, -5) == 0
    assert numero_mayor(11, 8) == 11
    assert numero_mayor(-11, -8) == -8
    assert numero_mayor(5, 5) == 0


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 5, 5),
        (6, 5, 6),
        (3, 3, 0),
        (-3, 3, 3),
        (-8, -2, -2),
        (119, 0, 119),
        (-119, 0, 0)
    ]
)
def test_numero_mayor_params(input_n1, input_n2, expected):
    assert numero_mayor(input_n1, input_n2) == expected
