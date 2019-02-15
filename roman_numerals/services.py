import math


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

        self.symbols.update({
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        })

    def convert(self, num):

        if num in self.symbols.keys():
            return self.symbols[num]

        result = ""

        for i, threshold in enumerate(reversed(self.thresholds)):

            div_result = int(math.floor(num / threshold))
            deduction = div_result * threshold

            if div_result >= 1:

                if deduction in self.symbols.keys():
                    result += self.symbols[deduction]
                else:
                    for _ in range(div_result):
                        result += self.symbols[threshold]

                remaining_num = (num - deduction)

                result += self.convert(remaining_num)
                break

        return result


