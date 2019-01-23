
class Calculator(object):

    def __init__(self):
        super(Calculator, self).__init__()

    def add(self, numbers):

        numbers = numbers.strip()
        if not numbers:
            return 0

        if numbers.startswith("//"):
            delimeter_char = ""
            delimeter_index = 2

            while numbers[delimeter_index] != '\n':
                delimeter_char += numbers[delimeter_index]
                delimeter_index += 1

            delimeter_index += 1

            numbers = numbers[delimeter_index:]
        else:
            delimeter_char = ","

        sum_numbers = 0

        individual_numbers = numbers.replace("\n", delimeter_char).split(delimeter_char)

        negative_numbers = []
        for individual_number in individual_numbers:
            if not individual_number:
                raise Exception("invalid format")

            int_number = int(individual_number)
            if int_number < 0:
                negative_numbers.append(int_number)

            if int_number > 1000:
                continue

            sum_numbers += int_number

        if negative_numbers:
            raise Exception(" Negatives not allowed: " + ",".join([ str(neg_num) for neg_num in negative_numbers ]))

        return sum_numbers
