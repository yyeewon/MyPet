from django.contrib import admin

# Post model 불러옴
from .models import Post

# Register your models here.
# 관리자의 게시글 접근 가능
admin.site.register(Post)