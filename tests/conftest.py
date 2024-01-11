import pytest

from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

@pytest.fixture
def accum2():
    yield Accumulator()
    print("cleanup")

@pytest.fixture
def accum3(scope='session'):
    return Accumulator()