from django.db import models
from django.core.urlresolvers import reverse

class Computer(models.Model):

    def get_absolute_url(self):
        return reverse('computers:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return "Name: " + self.name+" Brand: "+self.brand+ " Price: " + self.price

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    computer_image = models.CharField(max_length=1000)
