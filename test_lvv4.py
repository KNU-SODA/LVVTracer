from LVVTracer import LVVTracer
import py7zr

def test_lvv_py7zr():
    testarg = "StarWars60.wav"
    with LVVTracer(target_func = "build_header") as traced:
        with py7zr.SevenZipFile("archive.7z", 'w') as archive:
            archive.writeall(testarg)

    answer = {'header': 4, 'filters': 1, 'password': 1}
    assert traced.getLVVmap() == answer
