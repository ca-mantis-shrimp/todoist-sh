"""Module for us to cloister away the SDK-specific code for use by the larger cli"""

from todoist_api_python.api import TodoistAPI


def get_tasks(api):
    """Given a working api, get all tasks for the API"""
    try:
        return api.get_tasks()
    except Exception as e:
        print(e)


def get_projects(api):
    """Given a working api, get all projects for the API"""
    try:
        return api.get_projects()
    except Exception as e:
        print(e)


def create_api(config):
    """Given a config, create a TodoistAPI object"""
    return TodoistAPI(config["security"]["key"])
