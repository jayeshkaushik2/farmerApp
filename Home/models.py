from django.db import models

# Create your models here.


class Farmer(models.Model):
    username = models.CharField(max_length=1000)
    tractorName = models.CharField(max_length=1000)
    


class Implement(models.Model):
    owner = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    harrow = models.BooleanField(blank=True, null=True, default=None)
    cultivator = models.BooleanField(blank=True, null=True, default=None)
    rotavator = models.BooleanField(blank=True, null=True, default=None)
    plough = models.BooleanField(blank=True, null=True, default=None)
    paddy_thrasher = models.BooleanField(blank=True, null=True, default=None)
    dumping_trailer = models.BooleanField(blank=True, null=True, default=None)
    wheel_trailer = models.BooleanField(blank=True, null=True, default=None)

    def __str__(self):
        return self.owner.username