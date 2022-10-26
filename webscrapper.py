from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re


def connect():
    connection_driver = webdriver.Chrome(ChromeDriverManager().install())
    connection_driver.get('https://www.flashscore.pl')
    connection_driver.maximize_window()
    time.sleep(4)
    return connection_driver


def move_to_previous_day(connection_driver):
    WebDriverWait(connection_driver, 20). \
        until(EC.element_to_be_clickable((By.XPATH,
                                          '//*[@id="live-table"]/div[1]/div[2]/div/div[1]'))).click()
    time.sleep(4)


def expand_all_hidden_blocks(connection_driver):
    elements = connection_driver.find_elements(By.CLASS_NAME, 'event__expanderBlock')
    # EXTENDS HIDDEN MATCHES
    for element in elements:
        if re.search(r'arrow event__expander event__expander--close', str(element.get_attribute('innerHTML'))):
            connection_driver.execute_script("arguments[0].click();", element)
            time.sleep(0.05)


def locate_matches_divs(connection_driver):
    html_source = connection_driver.page_source
    page_soup = soup(html_source, 'html.parser')
    matches_divs = page_soup.findAll('div', {'class': lambda value: value and value.startswith('event__match ')})
    return matches_divs


def collect_match_info(match):
    match_str = str(match)
    if re.search(r'Przełożone', match_str):
        return
    else:
        # SOMETIMES THERE IS NO INFO ABOUT HALF MATCH RESULT - THEN SKIP ALL MATCH AT THE BEGINNING OF LOOP

        try:
            half_goal_home = get_detail(match_str, 'half_goal_home')
            half_goal_away = get_detail(match_str, 'half_goal_away')
        except:
            return
        home_team = get_detail(match_str, 'home_team')
        away_team = get_detail(match_str, 'away_team')
        final_goal_home = get_detail(match_str, 'final_goal_home')
        final_goal_away = get_detail(match_str, 'final_goal_away')
        red_cards = check_red_cards(match_str)
        record_match_to_data(home_team, away_team, final_goal_home, final_goal_away, half_goal_home,
                             half_goal_away, red_cards)


def get_detail(match_under_analysis, detail):
    detail_dictionary_start = {
        'home_team': 'event__participant--home">',
        'home_team2': 'event__participant--home fontExtraBold">',
        'away_team': 'event__participant--away">',
        'away_team2': 'event__participant--away fontExtraBold">',
        'final_goal_home': 'class="event__score event__score--home">',
        'final_goal_away': 'class="event__score event__score--away">',
        'half_goal_home': 'class="event__part event__part--home event__part--1">(',
        'half_goal_away': 'class="event__part event__part--away event__part--1">(',
    }
    detail_dictionary_end = {
        'home_team': '<',
        'away_team': '<',
        'final_goal_home': '<',
        'final_goal_away': '<',
        'half_goal_home': ')',
        'half_goal_away': ')',
    }

    detail_searching_start = detail_dictionary_start[detail]
    detail_searching_end = detail_dictionary_end[detail]
    try:
        start = match_under_analysis.index(detail_searching_start)
    except:
        detail_searching_start = detail_dictionary_start[detail+'2']
        start = match_under_analysis.index(detail_searching_start)
    end = match_under_analysis.index(detail_searching_end, start)
    detail = match_under_analysis[start + len(detail_searching_start):end]
    return detail


def check_red_cards(match):
    if re.search(r'class="card-ico icon--redCard', match):
        cards = len(re.findall('class="card-ico icon--redCard', match))
    else:
        cards = 0
    return cards


def record_match_to_data(home_team, away_team, final_goal_home, final_goal_away, half_goal_home,
                         half_goal_away, red_cards):
    match = {
        'home_team': home_team,
        'away_team': away_team,
        'final_goal_home': final_goal_home,
        'final_goal_away': final_goal_away,
        'half_goal_home': half_goal_home,
        'half_goal_away': half_goal_away,
        'red_cards': red_cards
    }
    print(f'{home_team} {final_goal_home} ({half_goal_home}) -'
          f' {away_team} {final_goal_away} ({half_goal_away})')
    matches.append(match)


matches = []
driver = connect()
for i in range(1):
    move_to_previous_day(driver)
    expand_all_hidden_blocks(driver)
    matches_divs = locate_matches_divs(driver)
    for match in matches_divs:
        collect_match_info(match)