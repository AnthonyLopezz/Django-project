from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    image = models.ImageField(upload_to='ServicesApp')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
