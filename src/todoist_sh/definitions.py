import os
import shutil
import pathlib
import tomllib
import platformdirs

import dotenv

dotenv.load_dotenv()

API_KEY_ENVVAR = os.getenv("TODOIST_API_KEY")
ENCRYPTED_ENVVAR = os.getenv("TODOIST_SH_ENCRYPTED")

CONFIG_FILE_PATH = os.getenv("TODOIST_SH_CONFIG_FILE")

# Root directory of the project for navigation
ROOT_DIR = pathlib.Path(__file__).parent.parent.parent

DEFAUTS_DIR = ROOT_DIR / "defaults"
DEFAULT_CONFIG_FILE_PATH = DEFAUTS_DIR / "config.toml"

with open(ROOT_DIR / "pyproject.toml", "rb") as file:
    PROJECT_CONFIG = tomllib.load(file)

PROJECT_ATTRIBUTES = PROJECT_CONFIG["project"]
PROJECT_NAME = PROJECT_ATTRIBUTES["name"]
PROJECT_AUTHOR = PROJECT_ATTRIBUTES["authors"][0]["name"]

# Just for convenience in the mac/windows use-case
PLATFORM_DIRS = platformdirs.PlatformDirs(PROJECT_NAME, PROJECT_AUTHOR)

# We want to respect unix tradition while still putting it in the proper place for mac and windows
if os.name == "Linux":
    CONFIG_DIR = pathlib.Path(
        platformdirs.user_config_dir(PROJECT_NAME, PROJECT_AUTHOR)
    )
else:
    CONFIG_DIR = pathlib.Path(PLATFORM_DIRS.user_data_dir)
USER_CONFIG_FILE_PATH = CONFIG_DIR / "config.toml"

# If the app folder doesnt exist, create it, and copy the default config there for convenience
if not CONFIG_DIR.exists():
    CONFIG_DIR.mkdir(parents=True)
    shutil.copy(DEFAULT_CONFIG_FILE_PATH, USER_CONFIG_FILE_PATH)
