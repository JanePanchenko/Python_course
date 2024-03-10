class Writer:

    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.data = None

    def write_file(self, row: str) -> None:
        with open(self.__file_path, 'a') as writer:
            writer.write(row)
            self.data = row
