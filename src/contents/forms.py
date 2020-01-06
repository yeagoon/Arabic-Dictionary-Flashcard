from django import forms
from .models import ContentList, SearchHistory


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchHistory
        fields = [
            'search_word',
        ]


class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentList
        fields = [
            'arabic_word',
            'definition1',
            'definition2',
            'definition3',
            'definition4',
            'definition5',
        ]
