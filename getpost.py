from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, time
def getupdate(channel_id, database):
    if (sys.platform == 'win32'):
        driver = webdriver.Chrome('chromedriver.exe')
    else:
        driver = webdriver.Chrome()
    driver.get('https://weixin.sogou.com/weixin?type=1&s_from=input&query=' + channel_id + '&ie=utf8&_sug_=n&_sug_type_=')
    post = driver.find_element_by_css_selector('ul.news-list2 dl>dd>a')
    fake_url = post.get_attribute("href")
    post_title = post.get_attribute("text")
    if post_title not in database:
        time.sleep(0.5)
        driver.get(fake_url)
        true_url = driver.current_url
        driver.close()
        return post_title, true_url, channel_id
    else:
        driver.close()
        return 0