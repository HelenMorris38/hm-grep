def load_txt_file(filename):
    with open(filename,'r') as f:
        contents = f.read()
        return contents