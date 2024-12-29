from todoist_api_python.api import TodoistAPI

from dotenv import load_dotenv
import os
import argparse
import keyring
from keyrings.cryptfile.cryptfile import CryptFileKeyring


def process_task_command(args):
    if args.task_command == "list":
        return get_tasks(TodoistAPI(get_api_key()))
    else:
        return print("nothing to do")


def process_project_command(args):
    if args.project_command == "list":
        return get_projects(TodoistAPI(get_api_key()))
    else:
        return print("nothing to do")


parser = argparse.ArgumentParser(
    prog="tdst", description="A simple todoist CLI", epilog="Get Things Done!"
)
subcommands = parser.add_subparsers(help="top-level subcommands", required=True)
task_parser = subcommands.add_parser("tasks", help="get all tasks")
task_argument = task_parser.add_argument(
    "task_command",
    choices=("list", "add", "update"),
    help="the task command to run",
)
task_parser.set_defaults(func=process_task_command)

project_parser = subcommands.add_parser("projects", help="get all tasks")
project_argument = project_parser.add_argument(
    "project_command",
    choices=("list", "add", "update"),
    help="the project command to run",
)
project_parser.set_defaults(func=process_project_command)

key_parser = subcommands.add_parser("set-key", help="manually set api key")
key_parser.add_argument("api_key", help="todoist api key")

kr = CryptFileKeyring()


def run():
    args = parser.parse_args()
    args.func(args)

    # if args.tasks or args.projects is True:
    #     api_key = get_api_key()
    #     api = TodoistAPI(api_key)
    #
    #     if args.tasks is True:
    #         tasks = get_tasks(api)
    #         print(tasks)
    #
    #     if args.projects is True:
    #         projects = get_projects(api)
    #         print(projects)
    #     else:
    #         print("No arguments provided")


def get_tasks(api):
    try:
        return api.get_tasks()
    except Exception as e:
        print(e)


def get_projects(api):
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
