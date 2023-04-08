import passthrough
from LVVTracer import LVVTracer
from unittest.mock import patch
import sys

def test_lvv_pyflac():
    testargs = ["prog", "StarWars60.wav"]
    with patch.object(sys, 'argv', testargs):
        with LVVTracer(target_func = "normalize_encoding") as traced:
            passthrough.main()

    answer = {'chars': 18, 'c': 15, 'punct': 9, 'encoding': 3}
    assert traced.getLVVmap() == answer
