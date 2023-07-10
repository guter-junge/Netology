import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

import re
import json
from pprint import pprint

def get_headers():
    return Headers(browser='chrome', os='win').generate()

def get_hrefs():
    hh_main_html = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2',
                                headers=get_headers()).text
    hh_main_soup = BeautifulSoup(hh_main_html, 'lxml')

    tag_all_vacancies = hh_main_soup.find_all('div', class_='vacancy-serp-item-body__main-info')

    hrefs = []
    for tag_vacancy in tag_all_vacancies:
        span_tags = tag_vacancy.find_all('span')
        for span_tag in span_tags:
            if span_tag.find('a'):
                href = span_tag.find('a')['href']
                hrefs.append(href)
    return hrefs

def parse_vacancy_data():
    hrefs = get_hrefs()
    parsed_vacancies = []
    for href in hrefs:
        vacancy_html = requests.get(href, headers=get_headers()).text
        vacancy_soup = BeautifulSoup(vacancy_html, 'lxml')
        vacancy_title = vacancy_soup.find('div', class_='vacancy-title')
        vacancy_company_name = vacancy_soup.find('span', class_='vacancy-company-name')
        vacancy_location = vacancy_soup.find('p', {'data-qa': 'vacancy-view-location'})
        vacancy_description = vacancy_soup.find('div', class_='vacancy-description')

        vacancy_description_li = vacancy_description.find_all('li')
        li_text = [li.text.lower().strip() for li in vacancy_description_li]
        li_text = ' '.join(li_text)
        pattern = re.compile(r'(?=.*flask)(?=.*django)', re.IGNORECASE)
        if pattern.search(li_text):
            salary = vacancy_title.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite')
            if salary:
                salary = salary.text.replace('\xa0', ' ')
            city = vacancy_location
            if city:
                city = vacancy_location.text
            else:
                vacancy_location = vacancy_soup.find('span', {'data-qa': 'vacancy-view-raw-address'})
                city = vacancy_location.text.split(',')[0]
            company_name = vacancy_company_name.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text.replace('\xa0', ' ')
            parsed_vacancies.append({'link': href, 'salary': salary, 'city': city, 'company_name': company_name})

    with open('parsed_vacancies_json', 'w', encoding='utf-8') as file:
        json.dump(parsed_vacancies, file, indent=4,ensure_ascii=False)

    return parsed_vacancies

if __name__ == '__main__':
    parse_vacancy_data()


