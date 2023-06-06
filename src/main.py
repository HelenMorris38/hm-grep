import re
from src.helpers import load_txt_file

def grep(strng, filename, command=""):
    contents = load_txt_file(filename)
    result = ""
    for line in contents:
        if strng in line:
            result += line + '\n'
    return result.rstrip('\n')

