from upper import make_uppercase
def test_make_uppercase():
    assert make_uppercase("hello world") == "HELLO WORLD"
    assert make_uppercase("python") == "PYTHON"
    assert make_uppercase("test") == "TEST"
    assert make_uppercase("") == ""
    assert make_uppercase("123") == "123"
    assert make_uppercase("!@#") == "!@#"