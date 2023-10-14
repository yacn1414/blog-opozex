from django.db import models

class Socials(models.Model):
    name = models.CharField(max_length=255)
    link =  models.URLField(max_length=200)
    

    class Meta:
        verbose_name = "شبکه مجازی"
        verbose_name_plural = "شبکه های مجازی"

    def __str__(self):
        return self.name

