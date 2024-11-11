from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField( null=True)
    image_url = models.CharField(max_length=100, null=True)
    video_url = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
