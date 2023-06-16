import re
from src.helpers import load_txt_file, get_file_names, search_multiple_files, search_file

def grep(search_term="", filename="", command="", invert_match=""):
    if command == "-r":
        filenames = get_file_names()
        search_results = [search_multiple_files(search_term, filename) for filename in filenames]
        return ''.join(search_results).rstrip('\n')
    else:
        return search_file(search_term, filename)
