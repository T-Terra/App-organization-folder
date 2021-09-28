import os.path
from lib.make_dir import make_dir
# import shutil
#from time import sleep


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]

# lendo os arquivos
def type_f(dir_files):
    for i, file in enumerate(dir_files):
        is_file = os.path.isfile(file)
        is_dir = os.path.isdir(file)
        # if is_file and file != 'botpasta.py':
        if is_file and file in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css'):
            print(f"{i + 1} - é um arquivo Python: {file}")
            make_dir('code')
        elif is_file and 'docx' in file:
            print(f"{i + 1} - é um arquivo Word: {file}")
            # os.rename(file, folder_file + file)
        elif is_file and 'pdf' in file:
            print(f"{i + 1} - é um arquivo PDF: {file}")
            # os.rename(file, folder_file + file)
        elif is_dir:
            print(f"{i} - é um diretório: {file}")
            # return f"{i}- é um diretório: {file}
