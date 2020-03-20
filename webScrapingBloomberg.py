import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def to_right_ascii(prima_pagina):
	pp = list(prima_pagina[0])
	for index, char in enumerate(pp):
		if char == "è" or char == "é":
			pp[index] = "e'"
		elif char == "ì":
			pp[index] = "i'"
		elif char == "ò":
			pp[index] = "o'"
		elif char == "à":
			pp[index] = "a'"
		elif char == "ù":
			pp[index] = "u'"
		elif char == '“' or char == "”":
			pp[index] = '"'
		elif char == "’":
			pp[index] = "'"
	prima_pagina = ''.join(pp)
	return prima_pagina

url = 'https://news.google.com/?hl=it&gl=IT&ceid=IT:it'
prima_pagina = ''
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
parsed = soup.findAll('a', {"class":"DY5T1d"})

url_world = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT%3Ait'
response = requests.get(url_world)
soup = BeautifulSoup(response.text, "html.parser")
parsed += soup.findAll('a', {"class":"DY5T1d"})

url_affari = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT%3Ait'
response = requests.get(url_affari)
soup = BeautifulSoup(response.text, "html.parser")
parsed += soup.findAll('a', {"class":"DY5T1d"})

url_italy = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT%3Ait'
response = requests.get(url_italy)
soup = BeautifulSoup(response.text, "html.parser")
parsed += soup.findAll('a', {"class":"DY5T1d"})

url_tec = 'https://news.google.com/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl=it&gl=IT&ceid=IT%3Ait'
response = requests.get(url_tec)
soup = BeautifulSoup(response.text, "html.parser")
parsed += soup.findAll('a', {"class":"DY5T1d"})

url_intra = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT%3Ait'
response = requests.get(url_intra)
soup = BeautifulSoup(response.text, "html.parser")
parsed += soup.findAll('a', {"class":"DY5T1d"})

url_sport = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT%3Ait'
response = requests.get(url_sport)
soup = BeautifulSoup(response.text, "html.parser")
parsed += soup.findAll('a', {"class":"DY5T1d"})

url_salute = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT%3Ait'
response = requests.get(url_salute)
soup = BeautifulSoup(response.text, "html.parser")
parsed += soup.findAll('a', {"class":"DY5T1d"})

url_dago = 'https://www.dagospia.com'
response = requests.get(url_dago)
soup = BeautifulSoup(response.text, "html.parser")
#parsed_dago = soup.findAll('h1', {"class":"titolo"}) #troppo lungo - rimosso per questo motivo
parsed_dago = soup.findAll('span', {"class":"titolo"})

for a in parsed:
	print(a.text)


for a in parsed_dago:
	print(a.text)

print(len(parsed))
print(len(parsed_dago))

n = 0
n2 = 0
flag = False

while True:
	if flag is True:
		parsed_n = parsed[n].text
		n = (n + 1) % len(parsed)
		flag = False
	else:
		parsed_n = parsed_dago[n2].text
		n2 = (n2 + 1) % len(parsed_dago)
		flag = True
	
	parsed_n = parsed_n.replace("\n", "").replace("À", "A'").replace("Ù", "U'").replace("È", "E'").replace("É", "E'").replace("Ì", "I'").replace("Ò", "O'").replace("è", "e'").replace("é", "e'").replace("ì", "i'").replace("ò", "o'").replace("à", "a'").replace("ù", "u'").replace("“", '"').replace("”", '"').replace("’", "'").replace("…", "...").replace("–", "-")
	if prima_pagina != parsed_n:
		prima_pagina = parsed_n
		print("Request sent to Banner with text: " + prima_pagina)
		r = requests.get(url = "http://192.168.1.111", params = {'msg':prima_pagina, 'no-cache':0})

	print(n)
	print(n2)
	timer = len(prima_pagina)/2
	print(timer)
	time.sleep(timer)
