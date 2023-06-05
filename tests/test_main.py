from src.main import grep

def test_grep_returns_whole_file_when_passed_emtpy_string():
    output = "Judas Priest\nAC/DC\nBlack Sabbath\nAerosmith\nIron Maiden"
    assert grep("", "test-rockbands.txt") == output
def test_grep_returns_lines_with_found_string():
    output = "Judas Priest\nBon Jovi\nJunkyard"
    assert grep("J", "rockbands.txt") == output
    assert grep("Ju", "rockbands.txt") == "Judas Priest\nJunkyard"
def test_returns_result_when_searching_for_symbols():
    assert grep("!", "symbols.txt") == "!"
    assert grep("&", "symbols.txt") == "&"