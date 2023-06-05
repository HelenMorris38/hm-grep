from src.main import grep

def test_grep_returns_whole_file_when_passed_emtpy_string():
    output = "Judas Priest\nAC/DC\nBlack Sabbath\nAerosmith\nIron Maiden"
    assert grep("", 'test-rockbands.txt') == output