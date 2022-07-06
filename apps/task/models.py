from django.db import models

from apps.common.models import BaseModel


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.CASCADE
    )
