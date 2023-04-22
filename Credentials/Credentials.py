from enum import Enum
from cryptography.fernet import Fernet
import base64

class CredentialList(Enum):
    SMTP_SERVER = 'smtp.gmail.com'
    SENDER_EMAIL = 'hachatonagh123@gmail.com'
    PASSWORD = 'vlmpfaflxnvuudfp'
    RECEIVER_EMAIL = 'wojtek.pasiu@gmail.com'



    with open('key.key', 'rb') as key_file:
        key = key_file.read()

    # _key = None
    #
    # @classmethod
    # def _get_key(cls):
    #     if cls._key is None:
    #         with open('secret.key', 'rb') as f:
    #             cls._key = f.read()
    #     return cls._key
    #
    # @classmethod
    # def get_value(cls, name):
    #     with open('credentials.txt', 'rb') as f:
    #         for line in f:
    #             key, value = line.strip().split(b':')
    #             if key == name.encode():
    #                 fernet = Fernet(cls._get_key())
    #                 return fernet.decrypt(value).decode()
    #     return None

    def encrypt_credentials(self):
        f = Fernet(key)
        encrypted_credentials = {}
        for credential in CredentialList:
            encrypted_credentials[credential.name] = f.encrypt(credential.value.encode()).decode()
        with open('encrypted_credentials.txt', 'w') as file:
            file.write(str(encrypted_credentials))