class FormulaError(Exception):
    def __init__(self, message):
        self.message = message


class WrongOperatorError(Exception):
    def __init__(self, message):
        self.message = message
