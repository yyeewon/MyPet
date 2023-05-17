from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting, new_post, remove_post

# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # 웹사이트의 첫 화면은 index 페이지, URL 이름 index
    path('', index, name='index'),

    # URL:/blog 접속하면 mypet 소개하기 게시판
    path('blog/', blog),

    # URL:/blog/숫자로 접속하면 mypet 소개하기 게시판-세부 페이지(posting)
    path('blog/<int:pk>', posting, name="posting"),


    # post 작성 페이지 연결
    path('blog/new_post/', new_post),

    # post 삭제 ( 글마다의 primary key로 view 연결)
    path('blog/<int:pk>/remove/', remove_post),
]

# 이미지 url 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)