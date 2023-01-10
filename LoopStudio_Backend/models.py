from django.db import models

# Create your models here.
class clients(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        db_table = 'client'