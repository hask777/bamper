import requests
from bs4 import BeautifulSoup
import json

core_url = 'https://bamper.by'

req = requests.get('https://bamper.by/catalog/modeli/').text

soup = BeautifulSoup(req, 'lxml')

titles = soup.find_all('h3', class_='title-2')

br_ = []
br = []

for title in titles:
    # print(title.text)
    brand_link = title.find('a').get('href')
    brand_name = title.text

    brands = dict(
        brand_link = core_url + brand_link,
        brand_name = brand_name
    )

    br_.append(brands)
    br.append(brand_name.strip())

    # with open('brands.json', 'w', encoding='utf-8') as f:
    #     json.dump(br_, f, indent=4, ensure_ascii=False)

    with open('br_list.json', 'w', encoding='utf-8') as f:
        json.dump(br, f, indent=4, ensure_ascii=False)

    # ml_ = []
    # md_links = []
    # md_names = []
    # final_md = []
    # req = requests.get(core_url + brand_link)

    # soup = BeautifulSoup(req.text, 'lxml')
    # uls = soup.select('ul.cat-list.col-sm-6')
    # for ul in uls:
    #     links  = ul.find_all('a')
        
    #     for a in links:
    #         print(a.text)
    #         md_names.append(a.text)

    #         with open(f'models{brand_name}.txt', 'w', encoding='utf-8') as f:
    #             f.write(str(md_names))