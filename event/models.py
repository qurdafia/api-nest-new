from django.db import models


class Attributes(models.Model):
    conf = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    key = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class Events(models.Model):
    deviceId = models.CharField(max_length=255)
    deviceName = models.CharField(max_length=255)
    idNumber = models.CharField(max_length=255)
    personName = models.CharField(max_length=255)
    attributes = models.ManyToManyField(Attributes, default=None, blank=True)
    # attributes = models.ForeignKey(Attributes, related_name='attributes', on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.deviceName
