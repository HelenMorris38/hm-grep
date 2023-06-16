from os import path, walk

def load_txt_file(filename):
    with open(filename,'r') as f:
        lines = [line.rstrip('\n') for line in f]
        return lines

def get_file_names():
    filenames = []
    for root, dirs, files in walk("./"):
        if 'venv' not in root:
            for file in files:
                if file.endswith(".txt"):
                    filenames.append(path.join(root, file))
    formatted_filenames = [filename[2:] for filename in filenames]

    return formatted_filenames

def search_file(search_term, filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        result = [line for line in lines if line.find(search_term) != -1]
        return ''.join(result).rstrip('\n')
    
# def search_file_contents(strng, contents, invert_match=""):
#     result = ""
#     for line in contents:
#             if strng in line:
#                 if invert_match:
#                     if invert_match not in line:
#                         result += line + '\n'
#                 else:
#                     result += line + '\n'
#     return result.rstrip('\n')

def search_multiple_files(strng, filename, contents, invert_match=""):
    result = ""
    for line in contents:
        if strng in line:
            if invert_match:
                if invert_match not in line:
                    result += filename + ':' + line + '\n'
            else:
                result += filename + ':' + line + '\n'
    return result


