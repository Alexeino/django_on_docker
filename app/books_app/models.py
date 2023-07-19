from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    pages = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=4)
    
    def __str__(self):
        return self.title