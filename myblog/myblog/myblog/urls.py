"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from article import views as article_vs
# from user import views as user_vs
from article.views import home_index, article_detail, article_list, article_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', home_index ),
    url(r'^article/',article_detail ),
    url( r'^list/', article_list),
    url( r'^detail/', article_detail),
    # url(r'aritcle_detail', article_vs.article_detail() ),
    # url(r'article_model', article_vs.article_model() ), 
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    # url( r'^template/article/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

