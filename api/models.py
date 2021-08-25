from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250, null=True, blank=True, default="No Description")
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
