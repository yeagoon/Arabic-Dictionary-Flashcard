from contents.models import ContentList, SearchHistory, CurrentFlashcard
from fetchword import body_dotranslate


def latest_word():
    i = 9
    obj = SearchHistory.objects.get(id=9)
    #
    print("This is a test. obj content is ", obj.search_word)
    #
    try:
        while obj is not None:
            i = i + 1
            if SearchHistory.objects.get(id=i) is None:
                break
            obj = SearchHistory.objects.get(id=i)
    except:
        print("You're in an exception")
        obj = SearchHistory.objects.get(id=i-1)

    translated_list = body_dotranslate.translate(obj.search_word)
    word_list = [i for i in range(6)]
    word_list[0] = obj.search_word
    for x in range(1, 6):
        if translated_list.head is None:
            word_list[x] = ''
        else:
            word_list[x] = translated_list.head.data
            translated_list.head = translated_list.head.next
    return word_list


def decrement_flashcard_num():
    obj = CurrentFlashcard.objects.get(id=1)
    sub_index = obj.current_index-1
    obj.current_index = sub_index
    obj.save()
    return sub_index


def increment_flashcard_num():
    obj = CurrentFlashcard.objects.get(id=1)
    added_index = obj.current_index+1
    obj.current_index = added_index
    obj.save()
    return added_index
