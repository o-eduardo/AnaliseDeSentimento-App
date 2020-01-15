from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
def check_exists_by_css(selector, driver):
    try:
        driver.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Firefox(executable_path=r'C:\GeckoDriver\geckodriver.exe')
link = "https://play.google.com/store/apps/details?id=com.astl.vidalink&hl=pt_BR"
#mostrar todos os reviews
driver.get(link + '&showAllReviews=true')
sleep(2)
print(driver.title)

while True:
    try:
        driver.find_element_by_css_selector('.RveJvd').click()
    except:
        for x in range(5):
            html = driver.find_element_by_tag_name('html')
            html.send_keys(Keys.END)
            sleep(2)

        if not check_exists_by_css('.RveJvd',driver):
            break


driver.quit()

