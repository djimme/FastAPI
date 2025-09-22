import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..", "src")))

import pytest
from model.explorer import Explorer
from error import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"]=":memory:"

from data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name = "LeeDJ",
        country="KR",
        description="Smart Korean"
    )

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample