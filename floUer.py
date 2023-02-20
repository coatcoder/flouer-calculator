import requests

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
#Добавить выбор сайта, проработать алгоритм для других сайтов.

def count_pages_opt_fp_ru():
    pg_nums_opt_fp_ru = []
    for i in range(1, 278):
        pg_nums_opt_fp_ru.append(i)
    return pg_nums_opt_fp_ru
def get_flower_opt_fp_ru(page_number):
    data = {}
    print("[+] Page number : ", page_number)
    page = requests.get("https://opt-fp.ru/catalog/srezannye-cvety",params=dict(page=page_number))
    html = page.text
    print("[+] Page selected : https://opt-fp.ru/catalog/srezannye-cvety?page=", page_number)
    parsed_html = BeautifulSoup(html, features="lxml")
    parsed_name = parsed_html.body.find_all('div', attrs={'class': 'product-box__name'})
    parsed_price = parsed_html.body.find_all('span', attrs={'class': 'price-result'})
    for i in range(0, len(parsed_price)):
        a = BeautifulSoup.get_text(parsed_name[i])
        name = a[1:-1]
        a = BeautifulSoup.get_text(parsed_price[i])
        price = a[26:-20]
        data[name] = price
    return data


