from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.blocking import BlockingScheduler

from config import settings
from apps.common.helpers import dramatiq_tasks_executor


class Command(BaseCommand):
    help = 'Run task scheduler'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            func=dramatiq_tasks_executor,
            # Execute every day at 00:00
            trigger=CronTrigger(hour='10', minute='38'),
            id="email_task_owners",
            max_instances=1,
            replace_existing=True,
            args=["apps.task.tasks.email_task_owners"],
        )

        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
