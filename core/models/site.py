from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=255)
    Logo1 = models.ImageField(upload_to='static/images/logo/')
    Logo2 = models.ImageField(upload_to='static/images/logo/')
    about = models.TextField()
    

    class Meta:
        verbose_name = "اطلاعات سایت"
        verbose_name_plural = "اطلاعات سایت"

    def __str__(self):
        return self.name

