from django.db import models
class IpAddress(models.Model):
    ips = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
    class Meta:
        verbose_name = "ip"
        verbose_name_plural = "ips"

    def __str__(self):
        return self.ips
