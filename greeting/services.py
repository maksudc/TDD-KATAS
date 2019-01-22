
def greet(name):

    prefix = "Hello, "

    text = ""
    if name:

        if isinstance(name, list):

            shouting_names = []
            normal_names = []

            for aname in name:
                if aname.upper() == aname:
                    shouting_names.append(aname)
                else:
                    normal_names.append(aname)

            if len(normal_names) > 0:

                comma_separated_ones = normal_names[0: len(name)-1]

                text = ", ".join(comma_separated_ones)

                if len(comma_separated_ones) > 1:
                    text += ","

                if len(normal_names) > 1:
                    text += " and "

                text += normal_names[-1]
                text += "."

            for i, ashouting_name in enumerate(shouting_names):

                text += " AND HELLO "

                text += ashouting_name
                text += "!"

                if i < len(shouting_names)-1:
                    text += " "
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

