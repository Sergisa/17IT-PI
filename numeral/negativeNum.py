from numeral.numeral import Numeral


class negativeNum(Numeral):

    def __init__(self, num):
        self.num = num * 2
        super().__init__()
