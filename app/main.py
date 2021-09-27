import os.path
from lib.type_file import type_f
# cria uma nova pasta
# os.makedirs("arquivo", mode=0o777, exist_ok=False)

#folder_file = "C:\\Users\\root\\Documents\\Bot\\arquivo\\"
folder_download = "C:\\Users\\root\\Downloads"
# pastaPara = "C:\\Users\\root\\Documents\\Bot\\Nova_pasta\\"
#root_dir = "C:\\Users\\root\\Documents\\Bot"
# pego o caminho do diretório
"""os.chdir(root_dir)
print("Tudo certo!!")"""

# lista todos os arquivos do diretório
files_dir = os.listdir(os.chdir(folder_download))

type_f(files_dir)