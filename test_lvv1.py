from LVVTracer import LVVTracer
from sha256 import generate_hash
from md5 import md5_me

def test_lvv_sha256():
    with LVVTracer(target_func = "generate_hash") as traced:
        encoded = "mysalt".encode()
        generate_hash(encoded).hex()

    answer = {'t': 128, 'message_schedule': 65, 'a': 65, 'b': 65, 'c': 65, 'd': 65, 'e': 65, 'f': 65, 'g': 65, 'h': 65, 't1': 64, 't2': 64, 'message': 52, 'term1': 48, 'schedule': 48, 'term2': 43, 'term3': 36, 'term4': 36, 'blocks': 2, 'h0': 2, 'h1': 2, 'h2': 2, 'h3': 2, 'h5': 2, 'h4': 2, 'h6': 2, 'h7': 2, 'length': 1, 'i': 1, 'message_block': 1}
    assert traced.getLVVmap() == answer

def test_lvv_md5():
    with LVVTracer(target_func = "md5_me") as traced:
        encoded = "mypepperoni".encode()
        md5_me(encoded).hex()

    answer = {'f': 128, 'a': 65, 'b': 65, 'c': 65, 'd': 65, 'i': 64, 'g': 64, 'a0': 2, 'b0': 2, 'c0': 2, 'd0': 2, 'message': 1, 'bit_string': 1, 'added_consts': 1, 'shift_amounts': 1, 'block_words': 1, 'digest': 1}
    assert traced.getLVVmap() == answer
