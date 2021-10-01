import os.path
from src.path import main_path
from logs.log import logs_msg


def make_dir(dir_: str):
    os.chdir(main_path)
    if os.path.exists(dir_):
        print('Diretório já existe!!')
        return os.getcwd() + os.sep + str(dir_)
    else:
        os.mkdir(str(f"{dir_}"))
        return os.getcwd() + os.sep + str(dir_)