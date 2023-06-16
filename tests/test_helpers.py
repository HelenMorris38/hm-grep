from src.helpers import load_txt_file, get_file_names, search_multiple_files, search_file

def test_load_txt_file_returns_contents_of_file():
    output = ['Judas Priest', 'AC/DC', 'Black Sabbath', 'Aerosmith', 'Iron Maiden']
    assert load_txt_file('test-rockbands.txt') == output
def test_get_file_names_returns_list_of_txt_file_paths():
    assert get_file_names() == ['symbols.txt', 'test-rockbands.txt', 'rockbands.txt', 'test.txt', 'test-subdir/BFS1985.txt']
def test_search_multiple_files():
    assert search_multiple_files('Nirvana', 'test-subdir/BFS1985.txt') == 'test-subdir/BFS1985.txt:Since Bruce Springsteen, Madonna, way before Nirvana\ntest-subdir/BFS1985.txt:On the radio was Springsteen, Madonna, way before Nirvana\ntest-subdir/BFS1985.txt:And bring back Springsteen, Madonna, way before Nirvana\ntest-subdir/BFS1985.txt:Bruce Springsteen, Madonna, way before Nirvana\n'
def test_search_file():
    assert search_file('Nirvana', 'rockbands.txt') == 'Nirvana'
    assert search_file('Nirvana', './test-subdir/BFS1985.txt') == 'Since Bruce Springsteen, Madonna, way before Nirvana\nOn the radio was Springsteen, Madonna, way before Nirvana\nAnd bring back Springsteen, Madonna, way before Nirvana\nBruce Springsteen, Madonna, way before Nirvana'