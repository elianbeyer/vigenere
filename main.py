from string import ascii_uppercase as eng_aplhabet

def encrypt(msg_key, table_key, plain_text):
    pass

def decrypt(msg_key, table_key, cipher_text):
    pass

def mk_keystream(key, msg_len):
    pass

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