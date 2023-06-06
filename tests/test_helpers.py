from src.helpers import load_txt_file, get_file_names

def test_load_txt_file_returns_contents_of_file():
    output = ['Judas Priest', 'AC/DC', 'Black Sabbath', 'Aerosmith', 'Iron Maiden']
    assert load_txt_file('test-rockbands.txt') == output
def test_get_file_names_returns_list_of_txt_file_paths():
    assert get_file_names() == ['symbols.txt', 'test-rockbands.txt', 'rockbands.txt', 'test.txt', 'test-subdir/BFS1985.txt']
