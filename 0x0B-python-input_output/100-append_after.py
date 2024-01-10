#!/usr/bin/python3
# This script contains the append_after function.

def append_after(filename="", search_string="", new_string=""):
    """
    Appends new_string to a file following each line containing search_string.

    :param filename: Path to the file
    :param search_string: String to search for within the file
    :param new_string: String to append after each occurrence of search_string
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        changed = []
        for line in lines:
            changed.append(line)
            if search_string in line:
                changed.append(new_string)

        file.seek(0)
        file.write("".join(changed))
