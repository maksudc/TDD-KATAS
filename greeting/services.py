
def greet(name):

    prefix = "Hello, "

    text = None
    if name:

        if isinstance(name, list):

            if len(name) > 1:
                comma_separated_ones = name[0: len(name)-1]

                text = ", ".join(comma_separated_ones)

                if len(comma_separated_ones) > 1:
                    text += ","
                    
                text += " and "
                text += name[-1]
                text += "."
        else:
            text = name

            if name.upper() == name:
                prefix = "HELLO "
                text += "!"
            else:
                text += "."
    else:
        text = "my friend."

    return prefix + text

