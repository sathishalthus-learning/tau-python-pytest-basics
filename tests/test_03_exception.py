import pytest


def test_expected_exception():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0

    assert 'division by zero' in str(e.value)