import os.path
from src.type_file import type_f
from src.path import folder_download
# cria uma nova pasta
# os.makedirs("arquivo", mode=0o777, exist_ok=False)

# lista todos os arquivos do diretório
files_dir = os.listdir(os.chdir(folder_download))

type_f(files_dir)
