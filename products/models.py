from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    title = models.CharField(default="例：用短视频记录美好生活", max_length=50)
    intro = models.TextField(default="在这里写app介绍")
    url = models.CharField(default="http://", max_length=100)
    icon = models.ImageField(default="default.png", upload_to="image/")
    image = models.ImageField(default="default.png", upload_to="image/")

    votes = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:60] + '...'
