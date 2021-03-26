from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    