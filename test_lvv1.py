# from LVVTracer import LVVTracer
from sha256 import generate_hash
from md5 import md5_me

def test_lvv_sha256():
    # with LVVTracer(target_func = "generate_hash") as traced:
    #     encoded = "mysalt".encode()
    #     generate_hash(encoded).hex()

    encoded = "mysalt".encode()
    generate_hash(encoded).hex()

    answer = {'t': 352, 'schedule': 270, 'term2': 266, 'term4': 258, 'h0': 226, 'h1': 226, 'h2': 226, 'h3': 226, 'h5': 226, 'h4': 226, 'h6': 226, 'h7': 226, 'message': 225, 'length': 225, 'blocks': 225, 'i': 225, 'message_block': 225, 'message_schedule': 225, 'term1': 224, 'term3': 223, 'a': 193, 'b': 193, 'c': 193, 'd': 193, 'e': 193, 'f': 193, 'g': 193, 'h': 193, 't1': 191, 't2': 127}
    assert {} == answer

def test_lvv_md5():
    with LVVTracer(target_func = "md5_me") as traced:
        encoded = "mypepperoni".encode()
        md5_me(encoded).hex()

    answer = {'f': 198, 'a': 151, 'c': 151, 'd': 151, 'i': 150, 'g': 150, 'message': 90, 'bit_string': 89, 'added_consts': 88, 'a0': 88, 'b0': 88, 'c0': 88, 'd0': 88, 'shift_amounts': 88, 'block_words': 87, 'b': 87, 'digest': 1}
    assert traced.getLVVmap() == answer
