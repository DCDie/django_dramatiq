import dramatiq
from django.core.mail import send_mail

from apps.task.models import Task
from config.settings import EMAIL_HOST_USER


@dramatiq.actor
def email_task_owners():
    emails = set(Task.objects.filter(completed=False).values_list('user__email', flat=True))
    send_mail(
        subject="Task",
        message="You have don't completed tasks",
        from_email=EMAIL_HOST_USER,
        recipient_list=emails,
        fail_silently=False,
    )
