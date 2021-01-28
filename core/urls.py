from django.contrib import admin
from django.urls import path
from blog.admin import blog_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls)
]
