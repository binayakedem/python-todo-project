from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=10)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name