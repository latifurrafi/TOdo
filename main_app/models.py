from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_data = models.DateField()
    due_time = models.TimeField(blank=True, null=True)

    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title