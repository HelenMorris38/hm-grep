from src.helpers import load_txt_file, get_file_names, search_file_contents, search_multiple_files

def test_load_txt_file_returns_contents_of_file():
    output = ['Judas Priest', 'AC/DC', 'Black Sabbath', 'Aerosmith', 'Iron Maiden']
    assert load_txt_file('test-rockbands.txt') == output
def test_get_file_names_returns_list_of_txt_file_paths():
    assert get_file_names() == ['symbols.txt', 'test-rockbands.txt', 'rockbands.txt', 'test.txt', 'test-subdir/BFS1985.txt']
def test_search_file_contents():
    contents = load_txt_file('rockbands.txt')
    assert search_file_contents('Nirvana', contents) == 'Nirvana'
    next_contents = load_txt_file('./test-subdir/BFS1985.txt')
    assert search_file_contents('Nirvana', next_contents) == 'Since Bruce Springsteen, Madonna, way before Nirvana\nOn the radio was Springsteen, Madonna, way before Nirvana\nAnd bring back Springsteen, Madonna, way before Nirvana\nBruce Springsteen, Madonna, way before Nirvana'
def test_search_file_contents_inverts_matches():
    contents = load_txt_file('rockbands.txt')
    assert search_file_contents('J', contents, 'P') == 'Bon Jovi\nJunkyard'
def test_search_multiple_files():
    contents = load_txt_file('./test-subdir/BFS1985.txt')
    assert search_multiple_files('Nirvana', 'test-subdir/BFS1985.txt', contents, 'Madonna') == ''
