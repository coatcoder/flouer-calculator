import requests

data = {}
page = requests.get("https://opt-fp.ru/catalog/srezannye-cvety")
htmla = page.text
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def get_flower():
    html = htmla
    parsed_html = BeautifulSoup(html, features="lxml")
    parsed_name = parsed_html.body.find_all('div', attrs={'class': 'product-box__name'})
    parsed_price = parsed_html.body.find_all('span', attrs={'class': 'price-result'})

    def get_info():
        def get_all():  # Ужасный код. Оптимизируй это пожалуйста. ЗАЧЕМ СТОЛЬКО ПРОЦЕДУР!!!
            for i in range(0, 14):
                a = BeautifulSoup.get_text(parsed_name[i])
                name = a[1:-1]
                a = BeautifulSoup.get_text(parsed_price[i])
                price = a[26:-20]
                data[name] = price
        get_all()
    get_info()