import os
import keyring
from keyrings.cryptfile.cryptfile import CryptFileKeyring
from todoist_sh.definitions import API_KEY_ENVVAR


def get_encrypted_api_key(config):
    """Set and Query local keyring for API key and attempt to get it out. if that fails, try to set it from one of the other valid methods, if that still yields a blank, then error with a value error"""
    create_local_keyring(config)
    if keyring.get_password("todoist", "api_key") is None:
        api_key = (
            API_KEY_ENVVAR
            or config["security"]["key"]
            or input("Enter API Key for Encryption")
        )
        if api_key is not None:
            set_todoist_key(api_key)
            return api_key
        else:
            raise ValueError("No API Key Found, Please enter it with a valid method")
    else:
        api_key = keyring.get_password("todoist", "api_key")
        return api_key


def create_local_keyring(config):
    """Create and set local keyring, doesnt return anything since the setting of the keyring is a side-effect"""
    kr = CryptFileKeyring()
    kr.keyring_key = (
        os.getenv("KEYRING_CRYPTFILE_PASSWORD")
        or config["security"]["crypt_file_password"]
        or keyring.getpass()
    )
    keyring.set_keyring(kr)
    return


def set_todoist_key(key):
    """set the keyring for the todoist api key with a given key value"""
    keyring.set_password("todoist", "api_key", key)
    return
