from django.db import models
from django.utils import timezone
# Create your models here.
class Entry(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    daycreated=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"