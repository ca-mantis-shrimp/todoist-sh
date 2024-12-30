"""argument parser for the CLI, primarly used for the built parser class"""

import argparse
from todoist_sh.commands import process_list_subcommand, process_api_key_subcommand

parser = argparse.ArgumentParser(
    prog="tdst", description="A simple todoist CLI", epilog="Get Things Done!"
)
parser.add_argument("-c", "--config", help="path to config TOML to use")
parser.add_argument("-k", "--key", help="the api key we are using for our operations")
parser.add_argument(
    "-e", "--encrypt", help="whether or not to encrypt the api key", type=bool
)
subcommands = parser.add_subparsers(
    title="top level subcommands",
    description="subcommands for the various item types in todoist",
    help="you must always use a subcommand in order to run the CLI",
    required=True,
)
list_parser = subcommands.add_parser("list", aliases=["l"], help="list various things")
list_argument = list_parser.add_argument(
    "list_command",
    choices=("tasks", "projects", "config"),
    help="the object type to list",
    default="projects",
)
list_parser.set_defaults(func=process_list_subcommand)

config_parser = subcommands.add_parser("set", aliases=["s"], help="get all tasks")

config_subcommands = config_parser.add_subparsers(
    title="Set Operations for configs",
    description="set options at the shell and have it reflected in the user config",
    help="choose from the various options and set the appropriate options at runtime",
)
api_key_parser = config_subcommands.add_parser(
    "set_key", aliases=["k"], help="set the api key for the config"
)
api_key_argument = api_key_parser.add_argument(
    "api_key",
    help="the key you want to save to your config",
)
api_key_parser.set_defaults(func=process_api_key_subcommand)
