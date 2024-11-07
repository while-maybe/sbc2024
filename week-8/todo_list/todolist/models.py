from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100) # task title
    description = models.TextField() # task description
    completed = models.BooleanField() # task status
    
    def __str__(self):
        return self.title
    