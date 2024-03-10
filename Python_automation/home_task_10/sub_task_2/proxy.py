from Python_automation.home_task_10.sub_task_2.reader import Reader
from Python_automation.home_task_10.sub_task_2.writer import Writer


class ProxyReaderWriter:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self.data = None

    def read(self) -> None:
        if self.data:
            return
        self.reader.read_file()
        self.data = self.reader.data

    def write(self, row) -> None:
        if self.writer.data == row:
            return
        self.writer.write_file(row)
        self.data = None
        self.reader.data = None
