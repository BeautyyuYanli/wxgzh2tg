from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, time, json
from config import subscribe_list
delay = 5
def update():
    # load driver and cookies
    if (sys.platform == 'win32'):
        driver = webdriver.Chrome('chromedriver.exe')
    else:
        driver = webdriver.Chrome()
    with open('cookies.json', 'r') as f:
        cookies = f.read()
    cookies = json.loads(cookies)
    driver.get('https://mp.weixin.qq.com/')
    for i in cookies:
        driver.add_cookie(i)

    # open editor page
    time.sleep(delay / 3)
    driver.get('https://mp.weixin.qq.com/')
    time.sleep(delay)
    driver.find_element_by_css_selector('#js_text_editor_tool_link > div > div').click()
    time.sleep(delay / 2)

    # search for articles
    update_pool = []
    for entry in subscribe_list:
        while 1:
            try:
                othergzh_button = driver.find_element_by_css_selector('.weui-desktop-btn.weui-desktop-btn_default')
            except:
                continue
            else:
                break
        othergzh_button.click()
        time.sleep(delay / 2)
        while 1:
            try:
                input_box = driver.find_element_by_css_selector('.link_dialog_panel .weui-desktop-form__input:nth-child(2)')
            except:
                continue
            else:
                break
        input_box.send_keys(entry)
        time.sleep(delay / 3)
        input_box.send_keys(Keys.ENTER)
        time.sleep(delay)
        while 1:
            try:
                gzh_entry = driver.find_element_by_css_selector('.link_dialog_panel li:nth-child(1)')
            except:
                continue
            else:
                break
        gzh_entry.click()
        time.sleep(delay * 1.5)
        while 1:
            try:
                article_entries = driver.find_elements_by_css_selector('.inner_link_article_item')
                if len(article_entries) == 0:
                    raise ValueError()
            except:
                continue
            else:
                break
        for article_entry in article_entries:
            while 1:
                try:
                    link_element = article_entry.find_element_by_css_selector('span:nth-child(3) > a')
                except:
                    continue
                else:
                    break
            while 1:
                try:
                    title_element = article_entry.find_element_by_css_selector('div.inner_link_article_title > span:nth-child(2)')
                except:
                    continue
                else:
                    break
            link = link_element.get_attribute('href')
            title = title_element.get_attribute('innerHTML')
            update_pool.append((title, link, entry))

    # close driver and cookies
    cookies = driver.get_cookies()
    cookies = json.dumps(cookies)
    with open('cookies.json', 'w') as f:
        f.write(cookies)
    driver.close()
    print('updated!')
    return(update_pool)

if __name__ == "__main__":
    subscribe_list = [
        'dut_su',
        'iduter',
        'ituaner',
        'dutcxy',
        'dutjiaowu',
    ]
    update()
