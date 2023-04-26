from LVVTracer import LVVTracer
import nayajson
from add_and_search import WordDictionary
from change_coin import coinChange
from longest_increasing_sequence import findLIS
from missing_ranges import missing_ranges


def test_lvv_json1():
    testjson = """
        [
            {
                "id": 1,
                "type": "message",
                "content": "Hello!"
            },
            {
                "id": 2,
                "type": "query",
                "user_name": "tarzan",
                "password": "not_jane"
            },
            {
                "id": 3,
                "type": "command",
                "action": "swing"
            }
        ]
    """
    with LVVTracer(target_func = "process_char") as traced:
        obj = nayajson.parse_string(testjson)

    # print(traced.getLVVmap())
    answer = {'token': 553, 'add_char': 553, 'next_state': 515, 'completed': 505, 'now_token': 505, 'advance': 478, 'char': 458, 'charcode': 458, 'is_delimiter': 458, 'state': 458}
    assert traced.getLVVmap() == answer


def test_lvv_json2():
    testjson = """
        {
            "id": 3,
            "type": "command",
            "action": "swing"
        }
    """
    with LVVTracer(target_func = "is_delimiter") as traced:
        obj = nayajson.parse_string(testjson)

    # print(traced.getLVVmap())
    answer = {'char': 6}
    assert traced.getLVVmap() == answer

def test_lvv_json3():
    testjson = """
        {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

    """
    with LVVTracer(target_func = "process_char") as traced:
        obj = nayajson.parse_string(testjson)

    # print(traced.getLVVmap())
    answer = {'token': 893, 'add_char': 893, 'next_state': 702, 'completed': 689, 'now_token': 685, 'advance': 650, 'char': 624, 'charcode': 624, 'is_delimiter': 624, 'state': 624}
    assert traced.getLVVmap() == answer

def test_lvv_missing_ranges():
    with LVVTracer(target_func = "missing_ranges") as traced:
        missing_ranges([3, 5], 1, 10)

    answer = {'res': 4, 'start': 3, 'n': 2, 'arr': 1, 'lo': 1, 'hi': 1}
    assert traced.getLVVmap() == answer

def test_lvv_add_and_search():
    obj = WordDictionary()
    obj.add_word("mad")
    obj.add_word("pad")

    with LVVTracer(target_func = "search") as traced:
        obj.search("pad")

    answer = {'self': 19, 'cur': 16, 'i': 3, 'letter': 3, 'word': 1, 'node': 1}
    assert traced.getLVVmap() == answer

def test_longest_increasing_sequence():
    with LVVTracer(target_func = "findLIS") as traced:
        findLIS([3, 1, 2, 1, 4, 3, 5])

    answer = {'j': 20, 'MAX': 12, 'track': 9, 'dp': 7, 'ans': 7, 'i': 6, 'ansList': 4, 'sequence': 1, 'compare': 1, 'n': 1}
    assert traced.getLVVmap() == answer

def test_coin_change():
    with LVVTracer(target_func="coinChange") as traced:
        coinChange(5, [1, 2, 5, 10, 20, 50, 100] )

    answer = {'j': 36, 'minCoins': 32, 'i': 6, 'centsNeeded': 1, 'coinValues': 1}
    assert traced.getLVVmap() == answer
