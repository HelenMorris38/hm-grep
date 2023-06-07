import re
from src.helpers import load_txt_file, get_file_names, search_file_contents

def grep(strng, filename, command=""):
    if command == "-r":
        filenames = get_file_names()
        result = []
        search_results = []
        for filename in filenames:
            contents = load_txt_file(filename)
            for line in contents:
                if strng in line:
                    search_results.append([filename + ':', line + '\n'])
            # search_results = search_file_contents(strng, contents)

        print(search_results)
        results = [''.join(search_result) for search_result in search_results]
            
        print(results)
        return ''.join(results).rstrip('\n')
    else:
        contents = load_txt_file(filename)
        return search_file_contents(strng, contents)

