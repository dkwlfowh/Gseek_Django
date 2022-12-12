from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.news, name='news'),
    path('detail/',views.detail,name='detail')
]