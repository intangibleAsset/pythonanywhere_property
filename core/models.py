from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    propertyReference = models.CharField(max_length=20, null=True, blank=True, unique=True)
    description = models.CharField(max_length=40)
    oic = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    exhibitRef = models.CharField(max_length=30)
    seizedDate = models.DateField()
    seizedTime = models.TimeField()
    seizedLocation = models.CharField(max_length=60)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home/tolca/property/media/', null=True, blank=False, verbose_name="add image")
    thumbnail = models.ImageField(upload_to='home/tolca/property/media/', null=True, blank=True)

    def __str__(self):
        return self.image.url
