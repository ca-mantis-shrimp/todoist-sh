"""The core command module, pulls everything together to run Todoist calls via the SDK"""

import tomlkit
import todoist_sh.config as cli_config
import todoist_sh.sdk as sdk
import todoist_sh.definitions as defs


def process_list_subcommand(args):
    """match list subcommands against the needed functions"""
    config = cli_config.process_config_and_key_args(args)
    match args.list_command:
        case "tasks":
            return print(sdk.get_tasks(sdk.create_api(config)))
        case "projects":
            return print(sdk.get_projects(sdk.create_api(config)))
        case "config":
            return print(config)
        case _:
            return print("nothing to do")


def process_api_key_subcommand(args):
    """take the key given as the new storage key and either save it in the encrypted keyring or in the config file"""
    config = cli_config.process_config_and_key_args(args)
    if args.encrypt or defs.ENCRYPTED_ENVVAR or config["security"]["encrypted"] is True:
        defs.cli_config.encrypt.set_todoist_key(args.api_key)
    else:
        existing_toml = tomlkit.loads(args.config or defs.USER_CONFIG_FILE_PATH)
        existing_toml["security"]["key"] = args.api_key or args.key
        tomlkit
        existing_toml.write()
