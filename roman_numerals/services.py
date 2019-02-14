
class RomanToDecimalService(object):

    def __init__(self):
        super(RomanToDecimalService, self).__init__()

        self.thresholds = [1, 5, 10, 50, 100, 500, 1000]
        self.symbols = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

    def convert(self, num):

        if num in self.thresholds:
            return self.symbols[num]

        result = ""
        if (num / 5) < 1:

            if num < 5 - 1:
                for _ in range(num):
                    result += self.symbols[1]
            else:
                return self.symbols[1] + self.symbols[5]

        return result


