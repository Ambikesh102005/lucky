from hello_2 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Ambikesh") == "hello, Ambikesh"
