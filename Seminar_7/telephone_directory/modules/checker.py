def check_mode(mode: str):
    """
    :param mode: Selected mode
    :return: False if mode is not valid, else int(mode)
    """
    if not mode.isdigit() or not int(mode) in (1, 2, 3, 4, 9):
        return False
    return int(mode)


def check_format(format_: str):
    """
    :param format_: Selected format
    :return: False if format is not valid, else int(format)
    """
    if not format_.isdigit() or not int(format_) in (1, 2):
        return False
    return int(format_)


def check_name_of_file(name: str):
    """
    :param name: Selected name
    :return: False if name is not valid, else name
    """
    if name.lower() == "database":
        return False
    elif not name.isalpha():
        return None
    return name
