from django.db import models, IntegrityError

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.title != "" and self.content != "":
            return super(Note, self).save(*args, **kwargs)

        # import pdb; pdb.set_trace()
        raise IntegrityError
