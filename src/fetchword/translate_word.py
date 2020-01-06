from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from .linked_list import LinkedList


def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def do_translate(the_arabic_word):
    chrome_path = r"C:\Users\kyg\Downloads\chromedriver_win32\chromedriver"
    browser = webdriver.Chrome(chrome_path)
    browser.get('https://en.bab.la/dictionary/arabic-english')
    search_word = browser.find_element_by_id('bablasearch')
    search_word.send_keys(the_arabic_word)

    search_word.send_keys(Keys.ENTER)

    content = browser.page_source
    soup = BeautifulSoup(content, 'html.parser')

    word = ""
    definition_block = ""
    block_list = LinkedList()

    for a in soup.findAll('div', attrs={'class': 'quick-result-overview'}):
        translation = a.text
        for char in translation:
            if char.isspace() and char != " ":
                if word == "Arabic":
                    block_list.append(definition_block)
                    break
                if word == "EN":
                    if definition_block != "":
                        if block_list.head is None:
                            block_list.head.data = definition_block
                        else:
                            block_list.append(definition_block)
                            definition_block = ""
                    word = ""
                elif word != "" and word.isspace() is False:
                    definition_block = definition_block + word + "\n"
                    word = ""
            elif is_english(char):
                word = word + char
    browser.quit()
    return block_list
