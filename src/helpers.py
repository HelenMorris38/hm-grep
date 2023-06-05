def load_txt_file(filename):
    with open(filename,'r') as f:
        lines = [line.rstrip('\n') for line in f]
        return lines