import re
from src.helpers import load_txt_file, get_file_names, search_file_contents, search_multiple_files

def grep(strng, filename, command=""):
    if command == "-r":
        filenames = get_file_names()
        search_results = ""
        for filename in filenames:
            contents = load_txt_file(filename)
            search_result = search_multiple_files(strng, filename, contents)
            if search_result:
                search_results += search_result
            # for line in contents:
            #     if strng in line:
            #         search_results.append([filename + ':', line + '\n'])
        print(search_results)
        # results = [''.join(search_result) for search_result in search_results]
        return search_results.rstrip('\n')
    else:
        contents = load_txt_file(filename)
        return search_file_contents(strng, contents)

