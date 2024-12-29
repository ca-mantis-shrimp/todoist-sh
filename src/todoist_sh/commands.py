from todoist_api_python.api import TodoistAPI
from todoist_sh.config import get_api_key


def process_task_command(args):
    if args.task_command == "list":
        return print(get_tasks(TodoistAPI(get_api_key())))
    else:
        return print("nothing to do")


def process_project_command(args):
    if args.project_command == "list":
        return get_projects(TodoistAPI(get_api_key()))
    else:
        return print("nothing to do")


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
