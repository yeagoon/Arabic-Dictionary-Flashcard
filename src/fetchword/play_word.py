from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_sound(word):
    chrome_path = r"C:\Users\kyg\Downloads\chromedriver_win32\chromedriver"
    browser = webdriver.Chrome(chrome_path)
    browser.get('https://forvo.com/languages/ar/')
    search_word = browser.find_element_by_id('word_search_header')
    search_word.send_keys(word)
    search_word.send_keys(Keys.ENTER)

    play_icon = browser.find_element_by_xpath("// *[ @ class = "play  icon-size-m"]")
    play_icon.click()

