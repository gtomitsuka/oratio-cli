from oratioignoreparser import OratioIgnoreParser


def test_oratioignoreparser_simple():
    rules = ["ignored.txt", "please/ignore/me.txt"]
    parser = OratioIgnoreParser()
    parser.extend_list(rules)
    assert parser.should_be_ignored("ignored.txt")
    assert parser.should_be_ignored("please/ignore/me.txt")
    assert parser.should_be_ignored("subdirectory/ignored.txt")
    assert parser.should_be_ignored("oratiomodule.tar.gz")
    assert not parser.should_be_ignored("ignored1.txt")
    assert not parser.should_be_ignored("please/ignore/not.txt")


def test_oratioignoreparser_wildcards():
    rules = ["ignored*.txt", "ignore.*", "*/ignore/me.txt", "ignore/*/me.txt"]
    parser = OratioIgnoreParser()
    parser.extend_list(rules)
    assert parser.should_be_ignored("ignored.txt")
    assert parser.should_be_ignored("please/ignore/me.txt")
    assert parser.should_be_ignored("ignored1.txt")
    assert parser.should_be_ignored("ignore.svg")
    assert parser.should_be_ignored("ignore/ignore/ignore/me.txt")
    assert not parser.should_be_ignored("ignored1.svg")


def test_oratioignoreparser_backslashes():
    rules = ["please/ignore/me.txt"]
    parser = OratioIgnoreParser()
    parser.extend_list(rules)
    assert parser.should_be_ignored("please\\ignore\\me.txt")
