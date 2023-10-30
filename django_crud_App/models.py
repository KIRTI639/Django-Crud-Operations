from django.db import models

# Create your models here.
class candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.id}/{self.name}/{self.country}"