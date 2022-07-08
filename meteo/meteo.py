import requests
import xmltodict

url = "https://vrijeme.hr/hrvatska_n.xml"

response = requests.get(url)

data = xmltodict.parse(response.content)

#print(data)