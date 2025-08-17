import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

# print(page)
# print(dir(page))

# print(type(page.text))
# print(page.text[100:200])

# soup = BeautifulSoup(page.content, "html.parser")

# card_list = soup.find_all(class_ = 'card-content')

# card_dict_list = []

# for card in card_list:
#     card_dict = {}

#     title = card.find(class_ = 'title')
#     card_dict['title'] = title

#     card_dict_list.append(card_dict)

# print(card_dict_list)

# job_titles = soup.find_all('h2')
# sub_titles = soup.find_all('h3')

# company_list = soup.find_all(class_ = 'subtitle')
# company_name_list = []

# for company in company_list:
#     company_name_list.append(company)


# first_company_name = soup.find(_class = 'is-6')

# company_attr_list = []

# for company in company_name_list:
#     company_attr_list.append(company.attrs['class'][2])

# print(company_attr_list)

# first_company_name = soup.find(class_ = 'subtitle')

# print(first_company_name.attrs)

# print(company_name_list)

# print(job_titles)
# print(type(job_titles[0]))

# for job_title in job_titles:
#     print(job_title.text)

# print(soup)
# print(dir(soup))

# for sub_title in sub_titles:
#     print(sub_title.text)