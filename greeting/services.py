
def greet(name):

    prefix = "Hello, "

    text = ""
    if name:

        if isinstance(name, list):

            shouting_names = []
            normal_names = []

            extracted_names = []

            for aname in name:

                if "\"\"" in aname:
                    aname = aname.replace("\"\"", "").strip()
                    extracted_names.append(aname)
                else:
                    comma_separated_parts = aname.split(",")

                    if comma_separated_parts:
                        for i, extracted_name in enumerate(comma_separated_parts):
                            extracted_names.append(extracted_name.strip())
                    else:
                        extracted_names.append(aname.strip())

            name = extracted_names

            for aname in name:
                if aname.upper() == aname:
                    shouting_names.append(aname)
                else:
                    normal_names.append(aname)

            if len(normal_names) > 0:

                comma_separated_ones = normal_names[0: len(normal_names)-1]

                text = ", ".join(comma_separated_ones)

                if len(comma_separated_ones) > 1:
                    text += ","

                if comma_separated_ones:
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

