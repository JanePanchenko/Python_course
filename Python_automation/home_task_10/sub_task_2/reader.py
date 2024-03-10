class Reader:

    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.data = None

    def read_file(self) -> None:
        with open(self.__file_path, 'r') as reader:
            self.data = reader.read()
