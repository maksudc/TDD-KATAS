import re

class Calculator(object):

    def __init__(self):
        super(Calculator, self).__init__()

    def add(self, numbers):

        numbers = numbers.strip()
        if not numbers:
            return 0

        delimeters = []
        if numbers.startswith("//"):
            entire_delimeter_str = ""
            delimeter_index = 2

            while numbers[delimeter_index] != '\n':
                entire_delimeter_str += numbers[delimeter_index]
                delimeter_index += 1

            if ('[' in entire_delimeter_str) and (']' in entire_delimeter_str):

                current_br_index = 0

                while current_br_index < len(entire_delimeter_str) and entire_delimeter_str[current_br_index] == '[':

                    current_delim = ""
                    current_br_index += 1

                    while current_br_index < len(entire_delimeter_str) and entire_delimeter_str[current_br_index] != ']':
                        if entire_delimeter_str[current_br_index].isalnum():
                            current_delim += entire_delimeter_str[current_br_index]
                        else:
                            current_delim += "\\" + entire_delimeter_str[current_br_index]

                        current_br_index += 1

                    delimeters.append(current_delim)
                    current_br_index += 1
            else:
                delimeters.append(entire_delimeter_str)

            delimeter_index += 1
            numbers = numbers[delimeter_index:]
        else:
            delimeters.append(",")
            delimeters.append("\n")

        sum_numbers = 0

        combined_regex_delimeter = "|".join(delimeters)
        print(combined_regex_delimeter)

        individual_numbers = re.split(combined_regex_delimeter, numbers)

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
