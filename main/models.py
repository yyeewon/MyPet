from django.db import models


# Create your models here.
class Post(models.Model):
    # postname: 제목, contents: 내용
    postname = models.CharField(max_length=50)
    # 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # postname -대체-> post object
    def __str__(self):
        return self.postname
