from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import re


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.flashscore.pl')
driver.maximize_window()
time.sleep(5)
elements = driver.find_elements(By.CLASS_NAME, 'event__expanderBlock')

# OPENS HIDDEN MATCHES
for element in elements:
    if re.search(r'arrow event__expander event__expander--close', str(element.get_attribute('innerHTML'))):
        print(element.get_attribute('innerHTML'))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.1)

htmlSource = driver.page_source
page_soup = soup(htmlSource, 'html.parser')
matches_divs = page_soup.findAll('div', {'class': lambda value: value and value.startswith('event__match '
                                                                                         'event__match--scheduled')})
for match in matches_divs:
    match_str = str(match)
    home_searching_start = 'event__participant--home">'
    home_searching_end = '</div>'
    start = match_str.index(home_searching_start)
    end = match_str.index(home_searching_end, start)
    home_team = match_str[start+len(home_searching_start):end]

    away_searching_start = 'event__participant--away">'
    away_searching_end = '</div>'
    start = match_str.index(away_searching_start)
    end = match_str.index(away_searching_end, start)
    away_team = match_str[start+len(away_searching_start):end]

    print(home_team+' - '+away_team)