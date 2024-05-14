from re import sub
from string import ascii_uppercase as eng_alphabet


def crypt(msg_key, table_key, text, encrypt=True):
    """
    En-/Decrypts a text using the vigenere cypher.

    :param msg_key: keyword
    :type msg_key: String
    :param table_key: keyword to make a keyed vigenere table
    :type table_key: String
    :param text: text to be en-/decrypted
    :type text: String
    :param encrypt: True if encryption, False if decryption
    :type encrypt: bool

    :return: cipher-/plaintext
    :rtype: String
    """
    vtable = VigenereTable(table_key)
    if encrypt:
        table = vtable.get_table()
    elif not encrypt:
        table = vtable.get_inv_table()
    out = ""
    text = text.upper()
    alphabet_set = set(eng_alphabet)
    keystream = mk_keystream(msg_key, len(text)).upper()
    keystream_index = 0
    for char in text:
        if char not in alphabet_set:
            out += char  # Keep non-alphabetic characters as is
        else:
            k = keystream[keystream_index]
            out += table[k][char]
            keystream_index += 1
    del vtable
    return out


def mk_keystream(key, msg_len):
    """
    Repeats String key until it matches msg_len.

    :param key: keyword
    :type key: String
    :param msg_len: Length
    :type msg_len: int

    :return: keystream
    :rtype: String
    """
    key_len = len(key)
    if key_len >= msg_len:
        return key[:msg_len]
    return (key * (msg_len % key_len + 1))[:msg_len]


def check_key(key):
    """
    Checks if a keyword only contains letters of the english alphabet.

    :param key: keyword to be checked
    :type key: String

    :return: Returns True if there are only english letters.
    :rtype: bool
    """
    return set(key.upper()) <= set(eng_alphabet)


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
        self.__inv_table = self.__mk_inv_table()

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
        alphabet = sub(f"[{key}]", "", eng_alphabet)

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
            high_lvl[key] = dict(zip(keys, shift_elms(alphabet, e)))

        return high_lvl

    def __mk_inv_table(self):
        """
        Creates the inverse vigenere table.

        :return: inverse vigenere table
        :rtype: dict{ String: dict{ String: String } }
        """
        inv_table = {}
        for key, low_lvl in self.__table.items():
            inv_table[key] = {v: k for k, v in low_lvl.items()}
        return inv_table

    def get_table(self):
        """
        Returns the table attribute.

        :return: vigenere table
        :rtype: dict{ String: dict{ String: String } }
        """
        return self.__table

    def get_inv_table(self):
        """
        Returns the inv_table attribute.

        :return: inverse vigenere table
        :rtype: dict{ String: dict{ String: String } }
        """
        return self.__inv_table

    def print_table(self, inverse=False):
        """
        Pretty prints the table.

        :param inverse: False for normal table, True for inverse table
        :type inverse: bool

        :return: None
        """
        if not inverse:
            for _, val in self.__table.items():
                print(''.join(val.values()))
        if inverse:
            for _, val in self.__inv_table.items():
                print(''.join(val.values()))


if __name__ == '__main__':
    print(crypt("hidden", "kryptos", "QKNEVW SKJJMSZ", False))
