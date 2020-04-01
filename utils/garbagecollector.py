import os

def dump(path):
    if os.path.isfile(path) or os.path.islink(file_path):
        os.remove(path)  
    elif os.path.isdir(path):
        shutil.rmtree(path)  
    else:
        raise ValueError("file {} is not a file or dir.".format(path))

