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

def check_repeating_letters(key):
    """
    Checks if a keyword contains letters multiple times.

    :param key: keyword to be checked
    :type key: String

    :return: Returns True if it does.
    :rtype: bool
    """
    for char in key:
        if key.count(char) > 1: return True
    return False

class VigenereTable:

    def __init__(self, key):
        self.__key = key
        self.__alphabet = self.__key_alphabet(self.__key)
        self.__table = self.__mk_table(self.__alphabet)

    def __key_alphabet(self, key):
        pass

    def __mk_table(self, alphabet):
        pass

    def get_table(self):
        return self.__table