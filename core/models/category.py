from django.db import models


class categories(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    t_post = models.IntegerField(default=0)
    

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title

