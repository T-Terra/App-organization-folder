import os.path

# lendo os arquivos
def type_f(dir_files):
    for i, file in enumerate(dir_files):
        is_file = os.path.isfile(file)
        is_dir = os.path.isdir(file)
        # if is_file and file != 'botpasta.py':
        if is_file and 'py' in file:
            print(f"{i+1} - é um arquivo Python: {file}")
        elif is_file and 'docx' in file:
            print(f"{i+1} - é um arquivo Word: {file}")
            # os.rename(file, folder_file + file)
        elif is_file and 'pdf' in file:
            print(f"{i+1} - é um arquivo PDF: {file}")
            # os.rename(file, folder_file + file)
        elif is_dir:
            print(f"{i} - é um diretório: {file}")
            #return f"{i}- é um diretório: {file}