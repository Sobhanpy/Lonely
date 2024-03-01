from django.db import models
from portfolio.models import Category


class Services(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="services", default="service.jpg")
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title