import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def to_right_ascii(prima_pagina):
	pp = list(prima_pagina)
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

url = 'https://www.ilpost.it/'
prima_pagina = ''
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
parsed = soup.findAll('a')
n = 24
while True:

	parsed_n = parsed[n]["title"]
	if parsed_n.startswith("Permalink"):
		n = n + 1
		parsed_n = parsed[n]["title"]
	if prima_pagina != parsed_n:
		prima_pagina = parsed_n
		prima_pagina = to_right_ascii(prima_pagina)
		print("Request sent to Banner with text: " + prima_pagina)
		r = requests.get(url = "http://192.168.2.117", params = {'msg':prima_pagina, 'no-cache':0})
	n += 1
	print(n)
	if n == 51:
		n = 24
	time.sleep(20)

