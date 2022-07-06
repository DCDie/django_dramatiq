from django.utils.module_loading import import_string


# Dramatiq tasks executor
def dramatiq_tasks_executor(task: str, *args, **kwargs):
    return import_string(task).send(**kwargs)
