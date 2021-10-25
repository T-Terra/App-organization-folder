def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


# extensions


CODE_EXT = ('py', 'js', 'php', 'html', 'sql', 'css')
OFFICE_EXT = ('docx', 'doc', 'xlsx', 'pptx')
PDF_EXT = 'pdf'
PHOTO_EXT = ('jpg', 'jpeg', 'gif', 'png', 'psd', 'ico')
TEXT_EXT = ('txt', 'log')
ZIP_EXT = ('zip', 'rar')
EXE_EXT = ('exe', 'inf', 'torrent', 'iss')
VIDEO_EXT = ('mp4', 'mp3', 'mkv', 'avi', 'mov')
OTHERS_EXT = ('ova', 'iso')


# Reading files
def is_code_file(event):
    if str.lower(extension_type(event)) in CODE_EXT:
        return True
    return False


def is_office_file(event):
    if str.lower(extension_type(event)) in OFFICE_EXT:
        return True
    return False


def is_pdf_file(event):
    if str.lower(extension_type(event)) in PDF_EXT:
        return True
    return False


def is_photo_file(event):
    if str.lower(extension_type(event)) in PHOTO_EXT:
        return True
    return False


def is_text_file(event):
    if str.lower(extension_type(event)) in TEXT_EXT:
        return True
    return False


def is_zip_file(event):
    if str.lower(extension_type(event)) in ZIP_EXT:
        return True
    return False


def is_exe_file(event):
    if str.lower(extension_type(event)) in EXE_EXT:
        return True
    return False


def is_video_file(event):
    if str.lower(extension_type(event)) in VIDEO_EXT:
        return True
    return False


def is_others_files(event):
    if str.lower(extension_type(event)) in OTHERS_EXT:
        return True
    return False
