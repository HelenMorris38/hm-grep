import re
from src.helpers import load_txt_file, get_file_names, search_file_contents

def grep(strng, filename, command=""):
    if command == "-r":
        filenames = get_file_names()
        result = ""
        for filename in filenames:
            contents = load_txt_file(filename)
            # search_results = []
            # for line in contents:
            #     if 'Nirvana' in line:
            #         print(line)
            #     if strng in line:
            #         search_results.append([filename, line])
            search_results = search_file_contents(strng, contents)
            if search_results:
                result += filename + ":" + search_results +'\n'
        print(result)
        return result
    else:
        contents = load_txt_file(filename)
        return search_file_contents(strng, contents)

