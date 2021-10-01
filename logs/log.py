import os


class logs_msg:
    def __init__(self, msg: str):
        self.msg = msg

        with open('file_log.txt', 'a') as file:
            file.write(self.msg)
            file.close()
