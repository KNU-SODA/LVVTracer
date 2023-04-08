import yaml
from LVVTracer import LVVTracer

def test_lvv_pyyaml():
    document = """
                  a: 1
                  b:
                    c: 3
                    d: 4
                """
    with LVVTracer(target_func = "write_plain") as traced:
        yaml.dump(yaml.load(document, Loader=yaml.FullLoader))

    answer = {'end': 21, 'ch': 21, 'start': 14, 'data': 10, 'self': 7, 'text': 7, 'split': 7, 'spaces': 7, 'breaks': 7}
    assert traced.getLVVmap() == answer
