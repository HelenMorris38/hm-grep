from os import listdir, path, walk

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
    return filenames


get_file_names()