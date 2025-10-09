from unittest import mock

import mod1
import mod2

def test_call_a():
    with mock.patch("mod1.preamble", return_value=""):
        assert "11" == mod2.summer(5, 6)

def test_call_b():
    with mock.patch("mod1.preamble") as mock_preamble:
        mock_preamble.return_value= ""
        assert "11" == mod2.summer(5, 6)

@mock.patch("mod1.preamble", return_value="")
def test_call_c(mock_preamble):
    assert "11" == mod2.summer(5, 6)

@mock.patch("mod1.preamble")
def test_call_d(mock_preamble):
    mock_preamble.return_value = ""
    assert "11" == mod2.summer(5, 6)
