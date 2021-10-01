
def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


# lendo os arquivos
def is_code_file(event):
    if extension_type(event) in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css'):
        return True
    return False


def is_office_file(event):
    if extension_type(event) in ('docx', 'doc', 'xlsx', 'pptx'):
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_photo_file(event):
    if extension_type(event) in ('jpg', 'jpeg', 'gif', 'png', 'psd', 'ico'):
        return True
    return False


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False


def is_zip_file(event):
    if extension_type(event) in ('zip', 'rar'):
        return True
    return False


def is_exe_file(event):
    if extension_type(event) in ('exe', 'inf', 'torrent'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mp4', 'mp3', 'mkv', 'avi', 'mov'):
        return True
    return False
