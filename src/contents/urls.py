from django.urls import path

from .views import (
    ContentsListView
)


app_name = 'contents'


urlpatterns = [
    path('', ContentsListView.as_view(), name='content_list')

]
