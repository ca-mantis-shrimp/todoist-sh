"""argument parser for the CLI, primarly used for the built parser class"""

import argparse
from todoist_sh.commands import process_task_command, process_project_command

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
task_parser = subcommands.add_parser("tasks", aliases=["ta"], help="get all tasks")
task_argument = task_parser.add_argument(
    "task_command",
    choices=("list", "add", "update"),
    help="the task command to run",
    default="list",
)
task_parser.set_defaults(func=process_task_command)

project_parser = subcommands.add_parser(
    "projects", aliases=["pr"], help="get all tasks"
)
project_argument = project_parser.add_argument(
    "project_command",
    choices=("list", "add", "update"),
    help="the project command to run",
    default="list",
)
project_parser.set_defaults(func=process_project_command)
