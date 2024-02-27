from django.db import models

class Smartphones(models.Model):
    price = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.name