import os.path
from src.path import folder_download


def make_dir(dir_: str):
    os.chdir(folder_download)
    if os.path.exists(dir_) == True:
        print('Diretório já existe!!')
        return os.getcwd() + os.sep + str(dir_)
    else:
        os.mkdir(str(f"{dir_}"))
        return os.getcwd() + os.sep + str(dir_)