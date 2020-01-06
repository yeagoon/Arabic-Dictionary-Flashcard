"""arabdic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from contents.views import content_create_view, button_clicked, flashcard_view, button_save, first_flashcard_view, next_flashcard_view, prev_flashcard_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content_create_view, name="search_page"),
    path('output/', button_clicked, name="script"),
    path('my flashcards next/', next_flashcard_view, name="flashcards_next"),
    path('my flashcards prev/', prev_flashcard_view, name="flashcards_prev"),
    path('my flashcard /', first_flashcard_view, name="first_flashcard"),
    path('contents/', include('contents.urls'), name="flashcard_page"),
    path('save content/', button_save, name="save")

]
