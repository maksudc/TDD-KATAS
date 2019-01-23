
class Calculator(object):

    def __init__(self):
        super(Calculator, self).__init__()

    def add(self, numbers):

        sum_numbers = 0

        individual_numbers = numbers.split(",")

        for individual_number in individual_numbers:
            if individual_number:
                sum_numbers += int(individual_number)

        return sum_numbers
