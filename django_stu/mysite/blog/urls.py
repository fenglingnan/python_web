
from django.urls import path,re_path,include
from blog import views
urlpatterns = [
    re_path(r'articles/(\d{4})$',views.articles_year),
    re_path(r'articles/(?P<year>\d{4})/(?P<month>\d{2})',views.articles_year_mon),
    path(r'register',views.register,name='reg')
]