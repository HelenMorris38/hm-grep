import re
from src.helpers import load_txt_file, get_file_names, search_file_contents

def grep(strng, filename, command=""):
    if command == "-r":
        filenames = get_file_names()
        search_results = []
        for filename in filenames:
            contents = load_txt_file(filename)
            for line in contents:
                if strng in line:
                    search_results.append([filename + ':', line + '\n'])
        results = [''.join(search_result) for search_result in search_results]
        return ''.join(results).rstrip('\n')
    else:
        contents = load_txt_file(filename)
        return search_file_contents(strng, contents)

