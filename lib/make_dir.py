import os.path


def make_dir(dir_: str):
    try:
        os.mkdir(str(f"{dir_}"))
    except FileExistsError:
        print("Diretório já existe")
