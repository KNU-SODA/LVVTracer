import LVVTracer
import math

def test_lvv1():
    with LVVTracer("gcd") as traced:
        math.gcd(214194320,325792347)

    assert traced.getLVVmap() == answer
