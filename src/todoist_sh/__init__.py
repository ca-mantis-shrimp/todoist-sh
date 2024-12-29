from todoist_api_python.api import TodoistAPI

from dotenv import load_dotenv
import os
import argparse
import keyring
from keyrings.cryptfile.cryptfile import CryptFileKeyring

parser = argparse.ArgumentParser(
    prog="tdst", description="A simple todoist CLI", epilog="Get Things Done!"
)

kr = CryptFileKeyring()


def run():
    api_key = get_api_key()
    print(get_tasks(api_key))


def get_tasks(api_key):
    api = TodoistAPI(api_key)
    try:
        return api.get_tasks()
    except Exception as e:
        print(e)


def get_api_key():
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
