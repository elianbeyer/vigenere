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
        """
        Generates a "Keyed Alphabet" using a keyword and the english alphabet. Generation works as follows: Duplicate
        Letters are removed from the keyword. Letters of the keyword are removed from the original alphabet. The keyword
        is appended to the front of the alphabet.

        :param key: keyword
        :type key: String

        :return: keyed alphabet
        :rtype: List
        """
        alphabet = sub(f"[{key}]", "", eng_aplhabet)


        def rm_dupes_str(str):
            """
            Removes duplicate Chars from a String.

            :param str: Original String
            :type str: String

            :return: Reformatted String containing only unique Chars
            :rtype: String
            """
            new = ""
            for c in str:
                if c not in new:
                    new = new + c
            return new

        key = list(rm_dupes_str(key))
        alphabet = list(alphabet)
        return key + alphabet

    def __mk_table(self, alphabet):
        """
        Creates a vigenere table.

        :param alphabet: Alphabet used to create table
        :type alphabet: List

        :return: vigenere table
        :rtype: dict{ String: dict{ String: String } }
        """
        keys = alphabet.copy()

        def shift_elms(lst, n):
            n = n % len(lst)
            return lst[n:] + lst[:n]

        high_lvl = {}  # 1-lvl nested dictionary
        for e, key in enumerate(keys):
            print(e)
            print(shift_elms(alphabet, e))
            high_lvl[key] = dict(zip(keys, shift_elms(alphabet, e)))

        return high_lvl

    def get_table(self):
        return self.__table

    def print_table(self):
        for _, val in self.__table.items():
            print(''.join(val.values()))


if __name__ == '__main__':
    V1 = VigenereTable("kryptos")
    V1.print_table()
