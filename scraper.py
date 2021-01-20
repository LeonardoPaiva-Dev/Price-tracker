import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.kanui.com.br/Shape-Santa-Cruz-Powerlyte---Gremlin-Patrol-Amarelo-6601027.html?size=8.35&gclid=CjwKCAiAo5qABhBdEiwAOtGmbseH7bvzGt35746ycx_c-1szSLMc2w-7OtaztEtcDJlqWDLImibaFhoCqzAQAvD_BwE'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.465'}

email = input("Digite seu email: ")
password = input("Digite sua senha: ")

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", {"class": "product-name"}).get_text()
    price = soup.find("span", {"class": "catalog-detail-price-value"}).get_text().replace(',', '').replace('R$', '').replace(' ', '').strip()
    converted_price = float(price[0:3]) 

    if(converted_price < 170):
        send_mail()


    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, password)

    subject = 'Preço caiuu'
    body = 'olha o link aqui https://www.kanui.com.br/Shape-Santa-Cruz-Powerlyte---Gremlin-Patrol-Amarelo-6601027.html?size=8.35&gclid=CjwKCAiAo5qABhBdEiwAOtGmbseH7bvzGt35746ycx_c-1szSLMc2w-7OtaztEtcDJlqWDLImibaFhoCqzAQAvD_BwE'
    

