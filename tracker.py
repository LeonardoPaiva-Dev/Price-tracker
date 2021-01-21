import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

response = requests.get('https://www.sessionstore.com.br/shape-baker-maple-8-5-preto-dourado', headers=headers)



soup = BeautifulSoup(response.content, 'html.parser')

soup.encode('utf-8')

email = input("Digite o email remetente: ")
password = input("Digite sua senha: ")
receiver = input("Digite o email destinatário: ")

def check_price():
  title = soup.find(id="titulo-produto").get_text()
  price = soup.find("span", {"class": "preco-atual"}).get_text().replace(',', '').replace('R$', '').replace(' ', '').strip()

  
  converted_price = float(price[0:3])
  print(converted_price)
  if(converted_price < 300):
    send_mail()


  print(title.strip())


def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(email, password)

  subject = 'Preco caiu'
  body = "Segue o link https://www.sessionstore.com.br/shape-baker-maple-8-5-preto-dourado"

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    email,
    receiver,
    msg
  )
 
  print('email enviado')

  server.quit()


check_price()
  