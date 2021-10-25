import os
from time import sleep

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from src.make_dir import make_dir
from src.move_files import move_to_new_folder
from src.type_file import *
from src.path import main_path


class manipulando_evento(FileSystemEventHandler):

    def on_modified(self, event):
        if os.path.isdir(event.src_path):
            return
        if is_code_file(event):
            path_to_folder = make_dir('code')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_office_file(event):
            path_to_folder = make_dir('Arquivos_office')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_pdf_file(event):
            path_to_folder = make_dir('PDF')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_text_file(event):
            path_to_folder = make_dir('TXT')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_photo_file(event):
            path_to_folder = make_dir('Imagens')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_zip_file(event):
            path_to_folder = make_dir('ZIP')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_exe_file(event):
            path_to_folder = make_dir('exe')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_video_file(event):
            path_to_folder = make_dir('Vídeos')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_others_files(event):
            path_to_folder = make_dir('Outros')
            move_to_new_folder(event, path_to_folder)
            return


eventos = manipulando_evento()
observer = Observer()
observer.schedule(eventos, main_path, recursive=True)
observer.start()
try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    observer.unschedule(eventos)
    observer.stop()
finally:
    observer.join()
