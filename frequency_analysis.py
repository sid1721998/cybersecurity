import os
import string
import file_io

MAPPING_PATH = "./decryption_mapping.json"
USE_EXISTING_MAPPING = True
GENERATED_PLAIN_PATH = "./generated_plain.txt"


def count_frequencies(text, alphabet=list(string.ascii_lowercase)):
    """
    This function will receive a text, that does not contain uppercase letters (only
    lowercase and space + newline + special signs) and will create a dictionary, where:
        * the keys are all the lowercase letters in the alphabet
        * the values are the relative frequency of the letters in the supplied text

    Args:
        text (str): a text
        alphabet (list): this is a list of all lowercase letters in the English alphabet
    Returns:
        (dict): a dictionary that contains the relative frequency (value) of all the
            letters (keys)
    """

    freqs = {}
    for char in text.lower():
        if char in alphabet:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
    for char in alphabet:
        if char not in freqs:
            freqs[char] = 0
    return freqs


def sort_letters(freqs):
    """
    Given a dictionary with relative frequencies / probabilities this function will generate
    the list of all lowercase letters, that are sorted from most probably to least probably and
    return it.

    Args:
        freqs (dict): the dictionary containing the letters (keys) with their relative frequencies (values)
    Returns:
        (list): a list of all lowercase letters, sorted from most to least likely

    """

    return sorted(freqs, key=freqs.get, reverse=True)


def create_mapping(sorted_keys, sorted_values):
    """
    Given two sorted lower-case lists, it will create a dictionary where the
    first lists represents the keys and the second lists the values.

    Args:
        sorted_keys (list): a list containing all lowercase letters, that will function as
            the keys of our dictionary
        sorted_values (list): a list containing all lowercase letters, that will function as
            the values of our dictionary

    """

    mapping = {}
    for i in range(len(sorted_keys)):
        mapping[sorted_keys[i]] = sorted_values[i]
    return mapping


def decrypt(cipher, mapping):
    """
    Given a cipher text, and a mapping between lowercase letters, this function will
    apply the mapping on the cipher text, thus decrypting it
    """

    plain = ""
    for char in cipher.lower():
        if char.isalpha():
            plain += mapping.get(char, char)
        else:
            plain += char
    return plain


if __name__ == "__main__":

    # load the cipher text, as well as the supplied json file with the frequencies
    # of all letter in the english language (given in lowercase format)
    cipher = file_io.read_txtfile("./cipher.txt")
    en_freqs = file_io.read_jsonfile("./english_letter_frequencies.json")

    print("=" * 20 + "CIPHER TEXT" + "=" * 20)
    print(cipher + "\n" * 3)

    # count the relative frequencies of letters in the cipher text
    cipher_freqs = count_frequencies(cipher)

    # sorted both the frequency dictionary to simple, sorted lists of lower case letters
    en_sorted = sort_letters(en_freqs)
    cipher_sorted = sort_letters(cipher_freqs)

    # check if a mapping json file already exists
    if USE_EXISTING_MAPPING and os.path.isfile(MAPPING_PATH):
        # if it does, use it instead of creating a new one
        mapping = file_io.read_jsonfile(MAPPING_PATH)


    else:  # if it does not ...
        # create the mapping between the two sorted lowercase letter lists
        mapping = create_mapping(cipher_sorted, en_sorted)

        # then save it
        file_io.write_jsonfile(mapping, MAPPING_PATH)

        # use the mapping to try to decrypt the cipher text
    plain = decrypt(cipher, mapping)

    # then print it, and save it
    print("=" * 20 + "GENERATED PLAIN TEXT" + "=" * 20)
    print(plain)
    file_io.write_txtfile(plain, GENERATED_PLAIN_PATH)