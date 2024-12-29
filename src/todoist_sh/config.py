from dotenv import load_dotenv
import os
import keyring

from keyrings.cryptfile.cryptfile import CryptFileKeyring


def get_api_key():
    kr = CryptFileKeyring()
    load_dotenv()
    kr.keyring_key = os.getenv("KEYRING_CRYPTFILE_PASSWORD") or keyring.getpass()
    keyring.set_keyring(kr)

    api_key = keyring.get_password("todoist", "api_key")
    if api_key is None:
        print("No API key stored in keychain. checking for api key...")
        api_key_env_var = os.getenv("TODOIST_API_KEY")
        if api_key_env_var is None:
            print(
                "No API key found in environment variables. please set it or run auth command"
            )
        else:
            keyring.set_password("todoist", "api_key", api_key_env_var)
            print("API key stored in keychain")
        return

    return keyring.get_password("todoist", "api_key")
