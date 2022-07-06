import requests
from bs4 import BeautifulSoup
import smtplib
import time

status = "Purple - $109.00 USD"

URL = 'https://kbdfans.com/collections/plate/products/65-cnc-aluminum-plate'
URL2 = 'https://kbdfans.com/collections/case/products/in-stocktofu-65-aluminum-case?variant=29337657376816'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

page = requests.get(URL2, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="ProductSelect-1883967193146").get_text()


while True:
	if status in title:
		send_mail()
		break
	#time.sleep()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login(sender, code)

	subject = 'Now in Stock!'
	body = 'Go buy it now at https://kbdfans.com/collections/plate/products/65-cnc-aluminum-plate'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(sender, recipient, msg)
	print("Email Has Gone Though")

	server.quit()


# Alu Plate 65% -- ProductSelect-2168839012400