"""Config module to handle every part of the config from grabbing the files, to checking environment variables, to even handling the encrypted bits so that everything is in one place"""

import todoist_sh.config.encrypt as encrypt

import todoist_sh.definitions as defs

import tomllib


def process_config_and_key_args(args):
    """the primary function to grab BOTH the user config as well as the api key from arguments if provided, defaults if not"""
    config = process_config_args(args)
    config["security"]["key"] = get_key(args, config)

    if config["security"]["key"] is None:
        raise ValueError("No API Key Found, Please enter it with a valid method")
    else:
        return config


def process_config_args(args):
    """given some arguments, determines if we need to find a custom config or just use the default file path and returns what is found"""
    config_path = defs.CONFIG_FILE_PATH or args.config
    if config_path is not None:
        return get_config_at_path(args.config)
    else:
        return get_config_at_path()


def get_config_at_path(path=defs.USER_CONFIG_FILE_PATH):
    """Given a path, assume it leads to a TOML file and return the contents as a dictionary, failures will result in an error"""
    try:
        file = open(path, "rb")
    except IOError:
        print(f"Could not find file at {path}")
    else:
        with file:
            return tomllib.load(file)


def get_key(args, config):
    if args.key is not None:
        return args.key
    elif args.encrypt or config["security"]["encrypted"] is True:
        return encrypt.get_encrypted_api_key(config)
    else:
        return (
            defs.API_KEY_ENVVAR
            or config["security"]["key"]
            or input("Please Give Todoist API Key")
        )
