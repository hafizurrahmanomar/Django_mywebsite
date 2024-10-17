from django.db import models

# Create your models here.

class MobilePhone(models.Model):
    brand = models.CharField(max_length=100,blank=False)
    model = models.CharField(max_length=50)
    describtion =models.TextField()
    price = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.brand
    class Meta:
        ordering =['id','brand']
    
    
