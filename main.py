from re import sub
from string import ascii_uppercase as eng_aplhabet

def encrypt(msg_key, table_key, plain_text):
    pass

def decrypt(msg_key, table_key, cipher_text):
    pass

def mk_keystream(key, msg_len):
    pass

def check_key(key):
    """
    Checks if a keyword only contains letters of the english alphabet.

    :param key: keyword to be checked
    :type key: String

    :return: Returns True if there are only english letters.
    :rtype: bool
    """
    return set(key.upper()) <= set(eng_aplhabet)

class VigenereTable:

    def __init__(self, key):
        try:
            if check_key(key):
                self.__key = key.upper()
            else:
                raise ValueError("Keyword not valid for Vigenere Table")
        except ValueError:
            self.__key = ""
        self.__alphabet = self.__key_alphabet(self.__key)
        self.__table = self.__mk_table(self.__alphabet)

    def __str__(self):
        return f"Vigenere Table Object (key hidden)"

    def __key_alphabet(self, key):
        alphabet = sub(key, "", eng_aplhabet)
        key = list(key)
        alphabet = list(alphabet)
        return key + alphabet

    def __mk_table(self, alphabet):
        pass

    def get_table(self):
        return self.__table

    def print_table(self):
        pass