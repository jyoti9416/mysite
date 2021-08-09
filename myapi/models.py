from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255,blank=False)
    
    def __str__(self) -> str:
        return self.name
