from . import translate_word


def translate(word):
    def_list = translate_word.do_translate(word)
    return def_list
