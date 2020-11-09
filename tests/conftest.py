import pytest
from stuff.accum import Accumulator

@pytest.fixture(scope="session")
def accum():
    print("Setup steps !!!!")
    yield Accumulator()
    print("Tear Down steps !!!!")