from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import cat
class posts(models.Model):
    title = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    caption = models.TextField()
    categories = models.ManyToManyField(cat)
    preview = models.ImageField(upload_to='static/images/')    
    date = models.DateField()
    slug = models.SlugField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts_detail", kwargs={"pk": self.pk})
