from django.contrib import admin
from .models import ContentList, SearchHistory, CurrentFlashcard
# Register your models here.


admin.site.register(ContentList)
admin.site.register(SearchHistory)
admin.site.register(CurrentFlashcard)