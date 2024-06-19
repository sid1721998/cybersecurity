import json


def read_txtfile(path_to_file):
    """
    This function, given a path to a text file, will read and import
    the text file and return it.

    Args:
        path_to_file (str): the path to the text file

    Returns:
        (str): the content of the text file

    """
    print(f"[*] Reading text file: '{path_to_file}'", end="... ")

    with open(path_to_file, 'r') as f:
        content = f.read()

    print("OK")
    return content


def write_txtfile(data, path_to_file):
    """
    This function, given a string and a path to file, will write the
    string into the supplied file.

    Args:
        data (str): the string that will be written into the created file
        path_to_file (str): the path to the text file
    """
    print(f"[*] Writing to text file: '{path_to_file}'", end="... ")

    with open(path_to_file, 'w') as f:
        f.write(data)

    print("OK")


def read_jsonfile(path_to_file):
    """
    This function, given a path to a json file, will read and import
    the json content and return it.

    Args:
        path_to_file (str): the path to the json file

    Returns:
        (dict): the content of the json file

    """
    print(f"[*] Reading JSON file: '{path_to_file}'", end="... ")

    with open(path_to_file, 'r') as f:
        data = json.load(f)

    print("OK")
    return data


def write_jsonfile(data, path_to_file):
    """
    This function, given a dictionary and a path to file, will write the
    dictionary into the supplied json file.

    Args:
        data (dict): the dictionary that will be written into the created json file
        path_to_file (str): the path to the json file
    """
    print(f"[*] Writing to JSON file: '{path_to_file}'", end="... ")

    with open(path_to_file, 'w') as f:
        json.dump(data, f)

    print("OK")