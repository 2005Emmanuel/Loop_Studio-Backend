from django.db import models

# Create your models here.
class Clients(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(default='python', max_length=100)
    
class Meta:
        db_table = 'Clients'
# class clients(models.Model):
#     fullname = models.CharField(max_length=60)
#     email = models.EmailField()
#     message = models.TextField()
    
#     class Meta:
#         db_table = 'client'