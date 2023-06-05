from src.helpers import load_txt_file

def test_load_txt_file_returns_contents_of_file():
    output = "Judas Priest\nAC/DC\nBlack Sabbath\nAerosmith\nIron Maiden"
    assert load_txt_file('test-rockbands.txt') == output