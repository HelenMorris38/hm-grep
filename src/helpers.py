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

def search_multiple_files(search_term, filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        result = ""
        for line in lines:
            if line.find(search_term) != -1:
                result += filename + ':' + line
        return result
