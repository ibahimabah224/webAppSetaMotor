from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class category(models.Model):
    name=models.CharField(max_length=255)
    date_add=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-date_add']
    def __str__(self):
        return self.name
    

class vehicule(models.Model):
    immatriculation=models.CharField(max_length=500)
    mark=models.CharField(max_length=255)
    describe=models.TextField()
    image=models.CharField(max_length=5000)
    date_add=models.DateTimeField(auto_now=True)
    category=ForeignKey(category,related_name='categorie',on_delete=models.CASCADE)
    price=models.FloatField()
    class Meta:
        ordering=['-date_add']
    def __str__(self):
        return self.mark



