import pytest
from stuff.accum import Accumulator

@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0

@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    print("Adding 1 to current value")
    accum.add(1)
    assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_cannot_add_count_directly(accum):
    with pytest.raises(AttributeError, match="can't set attribute") as e:
        accum.count = 10
    assert "can't set attribute" in str(e.value)