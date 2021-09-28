import shutil


def move_to_new_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print(f'Arquivo movido para {path_to_new_folder}')
    except:
        print('Arquivo não existe no diretório!')
        pass