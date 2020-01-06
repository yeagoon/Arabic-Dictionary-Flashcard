from django.shortcuts import render
from .forms import ContentForm, SearchForm
from .models import SearchHistory, ContentList, CurrentFlashcard
# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from . import sub_views


def content_create_view(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SearchForm()
    context = {
        'is_to_search': True,
        'form': form,
    }
    return render(request, "content_create.html", context)


def button_clicked(request):
    # i = 9
    # obj = SearchHistory.objects.get(id=9)
    # #
    # print("This is a test. obj content is ", obj.search_word)
    # #
    # try:
    #     while obj is not None:
    #         i = i + 1
    #         if SearchHistory.objects.get(id=i) is None:
    #             break
    #         obj = SearchHistory.objects.get(id=i)
    # except:
    #     print("You're in an exception")
    #     obj = SearchHistory.objects.get(id=i-1)
    #
    # translated_list = body_dotranslate.translate(obj.search_word)
    # word_list = [i for i in range(5)]
    # for x in range(5):
    #     if translated_list.head is None:
    #         word_list[x] = ''
    #     else:
    #         word_list[x] = translated_list.head.data
    #         translated_list.head = translated_list.head.next

    word_list = sub_views.latest_word()

    form = ContentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContentForm()

    # context = {
    #     'is_to_search': False,
    #     'arabicWord': obj.search_word,
    #     'def1':  word_list[0],
    #     'def2': word_list[1],
    #     'def3': word_list[2],
    #     'def4': word_list[3],
    #     'def5': word_list[4],
    #     'form': form,
    # }

    context = {
        'is_to_search': False,
        'arabicWord': word_list[0],
        'def1': word_list[1],
        'def2': word_list[2],
        'def3': word_list[3],
        'def4': word_list[4],
        'def5': word_list[5],
        'form': form,
    }

    return render(request, "content_create.html", context)


def button_save(request):
    word_list = sub_views.latest_word()
    ContentList.objects.create(arabic_word=word_list[0], definition1=word_list[1], definition2=word_list[2],
                               definition3=word_list[3], definition4=word_list[4], definition5=word_list[5])
    print("New definition has been saved")
    context = {
        'is_to_search': False,
    }
    return render(request, "content_create.html", context)


def flashcard_view(request, my_id):
    obj = ContentList.objects.get(id=my_id)
    context = {
        "object": obj
    }
    return render(request, "flashcard.html", context)


def first_flashcard_view(request):
    current_index = CurrentFlashcard.objects.get(id=1)
    current_index.current_index = 1
    current_index.save()
    obj = ContentList.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "flashcard.html", context)


def next_flashcard_view(request):
    next_flashcard_num = sub_views.increment_flashcard_num()
    print("This is next")
    obj = ContentList.objects.get(id=next_flashcard_num)
    context = {
        "object": obj
    }
    return render(request, "flashcard.html", context)


def prev_flashcard_view(request):
    prev_flashcard_num = sub_views.decrement_flashcard_num()
    print("This is previous")
    if prev_flashcard_num < 1:
        prev_flashcard_num = 1
    obj2 = ContentList.objects.get(id=prev_flashcard_num)
    context = {
        "object": obj2
    }
    return render(request, "flashcard.html", context)


class ContentsListView(ListView):
    template_name = 'articles_list.html'
    queryset = ContentList.objects.all()

