import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from src.make_dir import *
from src.move_files import *
from src.type_file import *


class manipulando_evento(FileSystemEventHandler):
    @staticmethod
    def on_created(event, **kwargs):
        pass

    def on_modified(self, event):
        if os.path.isdir(event.src_path):
            return
        if is_code_file(event) == True:
            path_to_folder = make_dir('code')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_office_file(event) == True:
            path_to_folder = make_dir('Arquivos_office')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_pdf_file(event) == True:
            path_to_folder = make_dir('PDF')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_text_file(event) == True:
            path_to_folder = make_dir('TXT')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_photo_file(event) == True:
            path_to_folder = make_dir('Imagens')
            move_to_new_folder(event, path_to_folder)
            return
        elif is_zip_file(event) == True:
            path_to_folder = make_dir('ZIP')
            move_to_new_folder(event, path_to_folder)
            return
    @staticmethod
    def on_moved(event, **kwargs):
        pass

    @staticmethod
    def on_deleted(event, **kwargs):
        pass


eventos = manipulando_evento()
observer = Observer()
observer.schedule(eventos, folder_download, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.unschedule(eventos)
    observer.stop()
finally:
    observer.join()