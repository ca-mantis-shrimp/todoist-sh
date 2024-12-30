"""The core command module, pulls everything together to run Todoist calls via the SDK"""

import todoist_sh.config as cli_config
import todoist_sh.sdk as sdk


def process_task_command(args):
    """match the tasks subcommand to run the appropriate function"""
    config = cli_config.process_config_and_key_args(args)
    match args.task_command:
        case "list":
            return print(sdk.get_tasks(sdk.create_api(config)))
        case _:
            return print("nothing to do")


def process_project_command(args):
    """match the projects subcommand to run the appropriate function"""
    config = cli_config.process_config_and_key_args(args)
    match args.project_command:
        case "list":
            return print(sdk.get_projects(sdk.create_api(config)))
        case _:
            return print("nothing to do")
