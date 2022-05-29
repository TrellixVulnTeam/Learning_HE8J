from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField (max_length= 200)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return "Todo:" + self.title + "({})".format("Done" and self.isCompleted)
