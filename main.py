import time
from selenium import webdriver

MAIN_PAGE = "https://aofsoru.com/tic204u-elektronik-ticaret-dersi-sinav-sorulari"


def main_links():
    the_links = []
    CSS_BUTTON_SELECTOR = "body > div.container > div.row > div.col-md-8 > div > table"
    # buttons = browser.find_element_by_css_selector(CSS_BUTTON_SELECTOR)
    buttons = browser.find_elements_by_css_selector("a.btn.btn-primary")
    for btn in buttons:
        link = btn.get_attribute("href")
        the_links.append(link)

    return the_links


def getQuizJPGs():

    # div#quiz

    browser.find_element_by_css_selector("div#quiz")


    return True


browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get(MAIN_PAGE)

# Close the popup banner after first visit of site
# Click to close button, wait until it become visible
again = True
while again:
    try:
        browser.find_element_by_id("popupBannerClose").click()
        again = False
    except:
        time.sleep(1)
        again = True


# The links of available test page links
available_pages = main_links()

for link in available_pages:
    browser.get(link)

