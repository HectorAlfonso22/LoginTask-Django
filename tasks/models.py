from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.content}'
